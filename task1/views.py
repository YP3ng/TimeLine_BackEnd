from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task1.task import calculate

@api_view(['GET'])
def my_view(request):
    # apply_async
    res = calculate.apply_async(
        [1], 
        #queue='test', 
        countdown=5,
    )
    print("id: ", res.id)
    print("state: ", res.state)


    drespond = [
        "apply_async",
        "delay",
    ]

    #res = calculate.delay(2)
    # res is an instance of asyncResult, need to convert
    # However, celery works
    return Response(drespond)
