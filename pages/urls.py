from django.urls import path
from . import views

urlspattern = [
    path('mypage/', views.pages)
]