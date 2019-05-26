from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Project,Profile

# Create your views here.
def index(request):
    date = dt.date.today()
    return render(request,'all-posts/index.html',{"date": date,})
