from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', userlist, name='userlist'),
]
