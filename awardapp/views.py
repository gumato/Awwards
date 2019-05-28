from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,ProjectForm,UploadForm

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.objects.all()
    profiles = Profile.objects.all()
    # rates = Rate.objects.all()
    return render(request,'index.html',{"date": date,})

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



def search(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        search_project = Project.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'projects':search_project})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
def post_new(request):

    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

    return render(request,'post_new.html',locals())

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('homePage')

    else:
        form = UploadForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_review(request,pk):
   project = get_object_or_404(Project, pk=pk)
   current_user = request.user
   if request.method == 'POST':
       form = ReviewForm(request.POST)
       if form.is_valid():
           design = form.cleaned_data['design']
           usability = form.cleaned_data['usability']
           content = form.cleaned_data['content']
           review = form.save(commit=False)
           review.project = project
           review.design = design
           review.usability = usability
           review.content = content
           review.save()
           return redirect('homePage')
   else:
       form = ReviewForm()
       return render(request,'review.html',{"user":current_user,"form":form})    




 

