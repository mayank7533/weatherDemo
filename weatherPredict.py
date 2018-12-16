# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:22:11 2018

@author: Mayan
"""
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


df=pd.read_csv("testset.csv",skipinitialspace=True)

df['_hum'] = df['_hum'].fillna(df['_hum'].mean())
df.isnull().sum()

def preprocessing():
    global df
    #converting into datetime object
    dtime=pd.to_datetime(df['datetime_utc'])
    
    #extracting year, month, day, hour
    df['year']=dtime.dt.year
    df['month']=dtime.dt.month
    df['day']=dtime.dt.day
    df['hour']=dtime.dt.hour
    
    #removing empty value
    df.dropna(subset=['_tempm'], inplace=True)
    
    #selecting weather on one time
    df2 = df[df.hour==9]
    df2 = df2[df.year!=2016]
    return df2

    
df_train = preprocessing()
columns_train=['month','day','hour', '_rain', '_snow','_hum']
columns_target=['_tempm']

x_train = df_train[columns_train]
y_train = df_train[columns_target]
 
x_test = df[df['hour']==9]
x_test = x_test[df.year==2016]

y_test = x_test[columns_target]

x_test = x_test[columns_train]


clf=svm.LinearSVC()
clf.fit(x_train,y_train)
pred=clf.predict(x_test)    
print(y_test['_tempm']-pred)
print(mean_squared_error(y_test['_tempm'],pred))

x_test.to_csv("x_test.csv")
pred = pd.DataFrame(pred, columns=["_tempm"])
pred.to_csv('pred.csv', index=False)
y_test.to_csv("y_test.csv")
