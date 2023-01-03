from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Take a request and return a respond
def say_hi(request):
    return HttpResponse('Hello World!')