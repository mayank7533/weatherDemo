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

def preprocessing():
    global df
    dtime=pd.to_datetime(df['datetime_utc'])
    df['year']=dtime.dt.year
    df['month']=dtime.dt.month
    df['day']=dtime.dt.day
    df['hour']=dtime.dt.hour
    df.dropna(subset=['_tempm'], inplace=True)
    df=df[df.hour==9]
    df=df[df.year==2000]
    
preprocessing()
columns_target=['year','month','day','hour']
columns_train=['_tempm']
x=df[columns_target]
y=df[columns_train]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
clf=svm.LinearSVC()
clf.fit(x_train,y_train)
pred=clf.predict(x_test)

print(y_test-pred)
print(mean_squared_error(y_test,pred))