from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string(request):
    return HttpResponse('this my string1')
def page1(request):
    return render(request,'page1.html')
def page2(request):
    return render(request,'page2.html')
    