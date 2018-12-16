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

#columns in dataframe
col_list = list(df.columns)

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


import seaborn as sns
df2 = df.groupby(['year', 'month']).mean().reset_index()[['year','month', '_tempm']]
df2 = df2.pivot("month", "year", "_tempm")
sns.heatmap(df2).get_figure().savefig("visuals/temp_map.png")


import seaborn as sns
df2 = df.groupby(['year', 'month']).mean().reset_index()[['year','month', '_hum']]
df2 = df2.pivot("month", "year", "_hum")
sns.heatmap(df2).get_figure().savefig("visuals/hum_map.png")



#Drawing a heatmap
def facet_heatmap(data, color,**kws):
    values=data.columns.values[3]
    data = data.pivot(index='day', columns='hour', values=values)
    sns.heatmap(data, cmap='coolwarm', **kws)

#Joining heatmaps of every month in a year 
def weather_calendar(year,weather): 
    dfyear = df[df['year']==year][['month', 'day', 'hour', weather]]
    vmin=dfyear[weather].min()
    vmax=dfyear[weather].max()
    with sns.plotting_context(font_scale=12):
        g = sns.FacetGrid(dfyear,col="month", col_wrap=3) #One heatmap per month
        g = g.map_dataframe(facet_heatmap,vmin=vmin, vmax=vmax)
        g.set_axis_labels('Hour', 'Day')
        plt.subplots_adjust(top=0.9)
        g.fig.suptitle('%s Calendar. Year: %s.' %(weather, year), fontsize=18)
        g.savefig("visuals/"+weather+"cal_"+str(year)+".png")
        plt.close(g)

for i in range(1997,2017):
    try:
        weather_calendar(i,'_hum')
        weather_calendar(i,'_rain')
        weather_calendar(i, '_tempm')
    except:
        pass
    