from django.shortcuts import render
from .models import UploadedImages
import face_recognition
import numpy as np
import hashlib

def home(request):
    ctx = {}
    return render(request, 'fdx_search/index.html',ctx)

def search(request):
    ctx = {}
    hasher = hashlib.md5()
    for chunk in request.FILES['file'].chunks():
           hasher.update(chunk)
    file_md5 = hasher.hexdigest()
    ctx['file_md5'] = file_md5
    return render(request, 'fdx_search/search.html',ctx)

def search1(request,slug11):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)

def search2(request,slug11,slug22):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)