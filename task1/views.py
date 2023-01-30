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
        #countdown=3,
    )
    print("--------------------We still work while sleeping--------------------")

    respond = [
        {
            'id': res.id,
            'state_pre': res.state,
            'result': res.get(),
            'state_after': res.state,
            'successful_after': res.successful(),
            'metadata': res.info,

        },
    ]

    print("------------------------------Job done------------------------------")
    return Response(respond)
