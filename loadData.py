from mongoengine import *
import csv

connect('engine')

class Data(Document):
    year=IntField()
    month=IntField()
    day=IntField()
    actual=IntField()
    predicted=IntField()

reader=csv.DictReader(open('datasets/x_test.csv'))
readerY=csv.DictReader(open('datasets/y_test.csv'))
readerPred=csv.DictReader(open('datasets/pred.csv'))
dict_list=[]
dict_listY=[]
dict_listPred=[]
temp=[]
for line in reader:
    dict_list.append(line)
for line in readerY:
    dict_listY.append(line)
for line in readerPred:
    dict_listPred.append(line)

n=len(dict_list)
for i in range(n):
    dict_list[i]["actualTemp"]=dict_listY[i]['_tempm']
    dict_list[i]["predictedTemp"]=dict_listPred[i]['_tempm']

for val in dict_list:
    print(val)
    dat=Data.objects.create(
        year=2016,
        month = val['month'],
        day = val['day'],
        actual = int(float(val['actualTemp'])),
        predicted = int(float(val['predictedTemp'])),
    )
    dat.save()
