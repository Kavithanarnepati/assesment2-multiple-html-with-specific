from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string2(request):
    return HttpResponse('this is my string')
def page3(request):
    return render(request,'page3.html')
def page4(request):
    return render(request,'page4.html')
