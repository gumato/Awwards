from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Project,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    date = dt.date.today()
    return render(request,'all-posts/index.html',{"date": date,})


# @login_required(login_url='/accounts/login/')
# def profile(request,profile_id):

