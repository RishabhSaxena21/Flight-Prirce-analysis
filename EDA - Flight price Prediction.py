#!/usr/bin/env python
# coding: utf-8

# # Flight Price Prediction 

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


train_df = pd.read_excel("Data_Train.xlsx")
train_df.head()


# In[3]:


test_df = pd.read_excel("Test_set.xlsx")
test_df.head()


# In[4]:


final_df = train_df.append(test_df)
final_df


# In[5]:


print("The number of rows and columns are :", final_df.shape)


# In[6]:


final_df.isnull().sum()


# In[7]:


final_df.info()


# In[8]:


final_df.head()


# In[9]:


final_df['Date'] = final_df['Date_of_Journey'].str.split("/").str[0]
final_df['Month'] = final_df['Date_of_Journey'].str.split("/").str[1]
final_df['Year'] = final_df['Date_of_Journey'].str.split("/").str[2]


# In[10]:


final_df.head()


# In[11]:


final_df['Date'] = final_df['Date'].astype(int)
final_df['Month'] = final_df['Month'].astype(int)
final_df['Year'] = final_df['Year'].astype(int)


# In[12]:


final_df.info()


# In[13]:


final_df.drop(['Date_of_Journey'], axis = 1, inplace = True)


# In[14]:


final_df


# In[15]:


final_df['Arrival_Time'] = final_df['Arrival_Time'].str.split(' ').str[0]


# In[16]:


final_df['arrival_hr'] = final_df['Arrival_Time'].str.split(':').str[0]
final_df['arrival_min'] = final_df['Arrival_Time'].str.split(':').str[1]


# In[17]:


final_df.head()


# In[18]:


final_df['arrival_hr'] = final_df['arrival_hr'].astype(int)
final_df['arrival_min'] = final_df['arrival_min'].astype(int)


# In[19]:


final_df.info()


# In[20]:


final_df.drop(['Arrival_Time'], axis = 1, inplace = True)


# In[21]:


final_df['Total_Stops'].unique()


# In[22]:


final_df['Total_Stops']=final_df['Total_Stops'].map({'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4, 'nan' : 1})


# In[23]:


final_df.drop(['Route'], axis = 1, inplace = True)


# In[24]:


final_df.head()


# In[25]:


final_df['Additional_Info'].unique()


# In[28]:


final_df.drop(['Duration'], axis = 1, inplace=True)


# In[29]:


final_df['Price'].isnull().sum()


# In[31]:


final_df['Price'] = final_df['Price'].fillna(final_df['Price'].mean())


# In[35]:


final_df['Airline'].unique()


# In[36]:


from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()


# In[37]:


final_df['Airline'] = LE.fit_transform(final_df['Airline'])
final_df['Source'] = LE.fit_transform(final_df['Source'])
final_df['Destination'] = LE.fit_transform(final_df['Destination'])
final_df['Additional_Info'] = LE.fit_transform(final_df['Additional_Info'])


# In[39]:


final_df.shape


# In[42]:


sns.barplot(x='Airline', y='Price', data=final_df)


# In[ ]:




