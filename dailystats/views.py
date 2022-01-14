from urllib import request
from django.shortcuts import render

# Create your views here.
def getHomepage(request):
    return render(request, 'homepage.html')