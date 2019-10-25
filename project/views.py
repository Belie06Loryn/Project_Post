from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def page(request):
    return render(request,'all-projects/index.html',{})

def submit(request):
    return render(request,'all-projects/submit.html',{})    
