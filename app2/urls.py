app_name='something'
from django.urls import path
from app2.views import *
urlpatterns=[
    path('string2/',string2,name='string2'),
    path('page3/',page3,name='page3'),
    path('page4/',page4,name='page4'),

]