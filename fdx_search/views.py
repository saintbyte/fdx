from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {}
    return render(request, 'fdx_search/index.html',ctx)

def search(request):
    ctx = {}
    return render(request, 'fdx_search/search.html',ctx)

