from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm,FotoForm,VotingForm
from .models import Profile,Foto,Voting


def page(request):
    images=Foto.objects.all()
    profile=Profile.objects.all()
    return render(request,'all-projects/index.html',{'images':images,'profile':profile})

def submit(request):
    return render(request,'all-projects/submit.html',{})    

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('profile_display')
    else:
        form =ProfileForm()
    return render(request, 'all-projects/profile.html', {"form": form}) 

@login_required(login_url='/accounts/login/')
def profile_display(request):
   current_user = request.user
   profile=Profile.objects.filter(username_id=current_user).first()
   print(profile)
   images=Foto.objects.filter(profile_id=current_user)
   return render(request, 'all-projects/post.html', {"images":images,"profile":profile})

@login_required(login_url='/accounts/login/')
def project(request):
    current_user = request.user
    if request.method == 'POST':
        form = FotoForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user= current_user
            project.save()
        return redirect('profile_display')
    else:
        form =FotoForm()
    return render(request, 'all-projects/project.html', {"form": form})    

@login_required(login_url='/accounts/login/')
def ProjectVote(request,pk):
    project = Foto.objects.get(id=pk)
    current_user = request.user
    project_rating = Voting.objects.filter(project=project).order_by("pk")
    current_user_id = request.user.id
    project_rated = Voting.objects.filter(user=current_user_id)

    design_mean_rating = []
    for d_rating in project_rating:
        design_mean_rating.append(d_rating.design)
    try:
        design_average = sum(design_mean_rating)/len(design_mean_rating)
        design_percent = design_average * 10
    except ZeroDivisionError:
        design_average = "0"
        design_percent = 0

    usability_mean_rating = []
    for u_rating in project_rating:
        usability_mean_rating.append(u_rating.usability)
    try:
        usability_average = sum(usability_mean_rating)/len(usability_mean_rating)
        usability_percent = usability_average *10
    except ZeroDivisionError:
        usability_average = "0"
        usability_percent = 0
    
    content_mean_rating = []
    for c_rating in project_rating:
        content_mean_rating.append(c_rating.content)
    try:
        content_average = sum(content_mean_rating)/len(content_mean_rating)
        content_percent = content_average * 10
    except ZeroDivisionError:
        content_average = "0"
        content_percent = 0
    form = VotingForm()

    context = {
        "project":project,
        "form":form,
        "project_rating":project_rating,
        "design_average":design_average,
        "content_average":content_average,
        "usability_average":usability_average,
        "usability_percent":usability_percent,
        "content_percent":content_percent,
        "design_percent":design_percent
    }
    return render(request, 'all-projects/projectvote.html', context)    

@login_required(login_url='/accounts/login/')
def Vote(request,pk):
    project = Foto.objects.get(id=pk)
    current_user = request.user
    project_rating = Voting.objects.filter(project=project).order_by("pk")
    current_user_id = request.user.id
    project_rated = Voting.objects.filter(user=current_user_id)
    if request.method == 'POST':
        form = VotingForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user= current_user
            project.save()
        return redirect('projectvote')
    else:
        form = VotingForm()
    return render(request, 'all-projects/projectvote.html',{"project":project,"form":form})

def search_results(request):
    if 'searchs' in request.GET and request.GET['searchs']:
        search = request.GET.get("searchs")
        searched = Foto.searchs(search)
        
        backend = f"{search}"
        
        return render(request, 'all-projects/search.html',{"backend":backend,"searchs":searched})
    
    else:
        backend = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"backend":backend})    