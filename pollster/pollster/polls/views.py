from django.shortcuts import render
from django.contrib import admin

def index(request):
    return render(request, 'polls/index.html') #returns the index.html template
