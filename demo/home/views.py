from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
import os

def index(request):
    months = []
    for i in range(12):
        months.append(i + 1)
    template=loader.get_template('home/index.html')
    context={}
    context['months']=months
    return HttpResponse(template.render(context,request))


def showData(request):
    month=request.GET['month']
    year=request.GET['year']
    data=Data.objects(month=month,year=year)
    print(data)
    details=[]

    for row in data:
        detail = {}
        detail['day']=row.day
        detail['actual']=row.actual
        detail['predicted']=row.predicted
        details.append(detail)
    template=loader.get_template('home/showData.html')
    context={}
    print(details)
    context['data']=details
    context['year']=year
    context['month']=month
    return HttpResponse(template.render(context,request))


def visuals(request):
    year =2006
    years_avb = [2006, 2007, 2008, 2009, 2010, 2012, 2013]
    template = loader.get_template("home/visuals.html")
    render_img = []
    if request.method=="GET":
        images = os.listdir("home/static/")
        try:
            for image in images:
                if(image.split("_")[-1]==str(year)+".png"):
                    render_img.append(image)
        except:
            pass
        return HttpResponse(template.render({"years_avb":years_avb,"images":render_img}, request))
    if request.method=="POST":
        print(request.POST)
        year = request.POST['year']
        print(year)
        images = os.listdir("home/static/")
        try:
            for image in images:
                if (image.split("_")[-1] == str(year) + ".png"):
                    render_img.append(image)
        except:
            pass
        return HttpResponse(template.render({"years_avb": years_avb, "images": render_img}, request))
# Create your views here.
