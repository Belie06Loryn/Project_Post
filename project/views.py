from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm,FotoForm
from .models import Profile,Foto


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
def profile_vote(request):
   images=Foto.objects.filter(id=id).first()
   return render(request, 'all-projects/projectvote.html', {"images":images})    