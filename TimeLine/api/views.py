from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    return Response(input)