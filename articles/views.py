from django import forms
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def articles_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles_list.html', {'articles':articles})

def article_details(request,slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    return render(request,'article_details.html',{'article':article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticleForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponse('article successfully saved')
    else:
        form = forms.CreateArticleForm()
    return render(request,'create.html', {'form':form})
