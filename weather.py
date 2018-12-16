# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:52:59 2018

@author: Mayan
"""
import pandas as pd
import matplotlib.pyplot as plt 
df=pd.read_csv("testset.csv",skipinitialspace=True)


dtime=pd.to_datetime(df['datetime_utc'])
df['year']=dtime.dt.year
df['month']=dtime.dt.month
df['day']=dtime.dt.day
df['hour']=dtime.dt.hour
print(df["month"],df["day"],df["hour"])    
df['temp']=df['_tempm']
df[df.year==1999][df.hour==9]['_tempm'].mean()
df[df.year==1999][df.hour==9].plot(x='month',y='_tempm')
plt.subplot2grid((1,1),(0,0))

for x in df['year'].unique():
    
    
    pv.plot
    #f[year==x].plot(x=)
    #f[df.year==x].plot(kind="kde",y='_tempm',x='month')
plt.legend(df['year'].unique())

df.columns

        
    