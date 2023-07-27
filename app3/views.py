from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string3(request):
    return HttpResponse('<h1>This is my third string</h1>')
def page5(request):
    return render(request,'page5.html')
def page6(request):
    return render(request,'page6.html')
