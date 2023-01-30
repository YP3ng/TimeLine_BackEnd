from django.urls import path
from . import views

urlpatterns = [
    path('/<str:input1>/<str:input2>', views.my_view),

]