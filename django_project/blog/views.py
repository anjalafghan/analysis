from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request(post, url, body=None, headers={})):
    return HttpResponse('<h1>Blog home </h1>')
