from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,ProjectForm

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.objects.all()
    profiles = Profile.objects.all()
    # rates = Rate.objects.all()
    return render(request,'all-posts/index.html',{"date": date,})

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                to_email = form.cleaned_data.get('email')
                return HttpResponse('Confirm your email address to complete registration')
           
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'Form':form})    


# @login_required(login_url='/accounts/login/')
# def profile(request,profile_id):

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
 

