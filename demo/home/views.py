from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader


def index(request):
    template=loader.get_template('home/index.html')
    return HttpResponse(template.render({},request))


def showData(request):
    month=request.GET['month']
    year=request.GET['year']
    data=Data.objects(month=month,year=year)
    print(data)


# Create your views here.
