
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[3]:

df=pd.read_csv('911.csv')


# In[4]:

df.info()


# In[5]:

df.head()


# In[7]:

df['zip'].value_counts().head(5)


# In[8]:

df['twp'].value_counts().head(5)


# In[9]:

df['title'].nunique()


# In[10]:

df['reason']=df['title'].apply(lambda title:title.split(':')[0])


# In[11]:

df['reason'].value_counts()


# In[12]:

sns.countplot(x='reason',data=df)


# In[17]:

type(df['timeStamp'].iloc[0])


# In[18]:

df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[19]:

type(df['timeStamp'].iloc[0])


# In[20]:

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[21]:

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[22]:

df['Day of Week'] = df['Day of Week'].map(dmap)


# In[23]:

df.head()


# In[24]:

sns.countplot(x='Day of Week',data=df)


# In[26]:

sns.countplot(x='Day of Week',data=df,hue='reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[27]:

sns.countplot(x='Month',data=df,hue='reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[28]:

bymonth=df.groupby('Month').count()


# In[29]:

bymonth.head()


# In[30]:

bymonth['lat'].plot()


# In[31]:

sns.lmplot(x='Month',y='twp',data=bymonth.reset_index())


# In[32]:

df['date']=df['timeStamp'].apply(lambda t:t.date())


# In[33]:

df.groupby('date').count().head()


# In[35]:

df.groupby('date').count()['lat'].plot()
plt.tight_layout()


# In[39]:

df[df['reason']=='Traffic'].groupby('date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[40]:

df[df['reason']=='Fire'].groupby('date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[41]:

df[df['reason']=='EMS'].groupby('date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()


# In[45]:

dayhour=df.groupby(by=['Day of Week','Hour']).count().unstack()['reason']


# In[46]:

dayhour.head()


# In[47]:

sns.heatmap(dayhour)


# In[48]:

sns.clustermap(dayhour)


# In[50]:

dayMonth = df.groupby(by=['Day of Week','Month']).count()['reason'].unstack()
dayMonth.head()


# In[51]:

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[ ]:



