from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task1.task import add, multiply
from time import sleep

@api_view(['GET'])
def my_view(request, input):
    lst = [input]
    # apply_async
    res1 = add.apply_async(
        lst, 
        #queue='test', 
        #countdown=3,
    )
    print("--------------------We still work while sleeping--------------------")
    while not res1.ready():
        print(f'State={res1.state}, info={res1.info}')
        sleep(1)
    # Built-in state override at the end, need DB or other backend to store state in-progress
    print(f'State={res1.state}, info={res1.info}')
    
    respond = [
        {
            'id1': res1.id,
            'result': res1.get(),
            'state_after': res1.state,
            'successful_after': res1.successful(),
            'metadata': res1.info,

        },
    ]
    # res2 = multiply.apply_async(
    #     [res1.get()],
    # )

    # print("-------------------------After second task--------------------------")
    
    # respond.append({
    #         'id2': res2.id,
    #         'state_pre': res2.state,
    #         'result': res2.get(),
    #         'state_after': res2.state,
    #         'successful_after': res2.successful(),
    #         'metadata': res2.info,
    #     })
    

    print("------------------------------Job done------------------------------")
    return Response(respond)
