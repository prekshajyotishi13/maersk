#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1
# 
# undefined
# 

# ## 1. Read Employee data in sampleEmployee dataframe

# In[95]:


import pandas as pd
df_pandas = pd.read_csv("us-500.csv")


# ## 

# ## 2. Using this sampleEmployee dataframe create 100X more data points and store it into employeeDF ( this will have 50,000 rows )

# In[96]:


dfEmployee = pd.concat([df_pandas]*100, ignore_index=True)


# ## concat first and last name to get full name

# In[97]:


dfEmployee["Emp_Name"]=dfEmployee["first_name"]+" "+dfEmployee["last_name"]


# ## 3. The company has to plan a vaccination drive and the priority will be based on employee population in a particular city
# (Therefore, count the number of employees in each city)

# In[98]:


dfCityEmployeeDensity=dfEmployee.groupby("city")['Emp_Name'].count().reset_index(name='Empcount').sort_values(['Empcount'], ascending=False) 


# ## 4.Create a dataframe of CityEmployeeDensity, the 1st city will be the one with maxium number of employees

# In[99]:


dfCityEmployeeDensity["Sequence"]=dfCityEmployeeDensity.Empcount.rank(method='dense', ascending=False).astype(int)
dfCityEmployeeDensity


# ## 5. Please create new dataframe by name "VaccinationDrivePlan" with all columns from employeeDF and additional column "Sequence" 
# ## 6. In Sequence Column populate the value from the CityEmployeeDensity Dataframe. Print this dataframe 

# In[100]:


dfVaccinationDrivePlan=dfEmployee.merge(dfCityEmployeeDensity, on='city', how='left')


# In[101]:


dfVaccinationplan=dfVaccinationDrivePlan.sort_values(['Sequence'])
dfVaccinationplan


# ## Create sequence ID based on sequence column to group 100 emloyees for vaccination

# In[102]:


dfVaccinationplan.insert(0, 'SquenceID', range(1, 1+len(dfVaccinationplan)))
dfVaccinationplan


# ## Added a column Day to show vaccination plan 

# In[103]:


dfVaccinationplan["VaccinationDay"]=pd.qcut(dfVaccinationplan.SquenceID,q=500, labels=range(1, 500+1))
dfVaccinationplan


# ## vaccination days per city

# In[107]:


dfVaccinationdayspercity=dfVaccinationplan.groupby("city").VaccinationDay.nunique()
dfVaccinationdayspercity

