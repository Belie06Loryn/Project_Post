from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile,Foto


def page(request):
    return render(request,'all-projects/index.html',{})

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