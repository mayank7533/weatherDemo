from django.conf.urls import url
from home import views

urlpatterns = [
url(r'visuals/', views.visuals,name='visuals'),
url(r'showData/',views.showData,name='showData'),

]