from django.shortcuts import render
from django.http import HttpResponse
from task1.task import calculate

def my_view(request, input1, input2):
    res = calculate(input1, input2).delay()

    return HttpResponse(res)
