from django.urls import path
from . import views

# Url config
urlpatterns = [
    path('hello/', views.say_hi),
    path('', views.say_hi)
]
