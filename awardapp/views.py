from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render(request,'welcome.html')
