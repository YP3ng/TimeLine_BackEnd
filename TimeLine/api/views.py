from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from TimeLine.DamianCodeDummy.runDCcode import run
# import sys
# sys.path.append()

# testing
def getRoutes(request):
    routes = [
        'GET /api',
    ]
    return JsonResponse(routes, safe = False)

@api_view(['GET'])
def getRestRoute(request):
    routes = [
        'GET /api',
        'GET /api/rest',
        'GET /api/rest/:Number'
    ]
    return Response(routes)

@api_view(['GET'])
def getNum(request, input):
    return Response(input+"awake")

# Test Damian dummy code
@api_view(['GET'])
def getOutcome(request):
    dummyJson = run()
    return Response(dummyJson)

# TL core functionalities
@api_view(['GET'])
def getTL(request, url):
    pass


