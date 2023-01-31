from django.urls import path
from . import views

urlpatterns = [
    path('in/<int:input>/', views.my_view),

]