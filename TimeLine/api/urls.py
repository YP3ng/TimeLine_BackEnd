from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rest', views.getRestRoute),
    path('rest/<str:input>', views.getNum),
    path('dummy', views.getOutcome),
]