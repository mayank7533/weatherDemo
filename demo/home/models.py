from django.db import models
from mongoengine import *

class Data(Document):
    year=IntField()
    month=IntField()
    day=IntField()
    actual=IntField()
    predicted=IntField()
