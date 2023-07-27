app_name='anything'
from django.urls import path
from app3.views import *
urlpatterns=[
    path('string3/',string3,name='string3'),
    path('page5/',page5,name='page5'),
    path('page6/',page6,name='page6'),
]