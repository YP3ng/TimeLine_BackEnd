from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api',
    ]
    return JsonResponse(routes, safe = False)