from django.shortcuts import render
from rest_framework.response import Response
from task1.task import calculate


def my_view(request, input):
    res = calculate.delay(input)

    # res is an instance of asyncResult, need to convert
    # However, celery works
    return Response(res)
