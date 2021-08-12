from django.http import request
from django.shortcuts import render

# Create your views here.
def app1(request):

    return render(request,'adi.html')

def app2(request):

    return render(request,'sec.html')
    