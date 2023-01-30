from django.urls import path
from . import views

urlpatterns = [
    path('<int:input>', views.my_view),

]