from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def findex(request):
    return render(request, "index.html")

def fhistoria(request):
    return render(request, "historia.html")




