from django.urls import path
from .templates.quotes import views

urlpatterns = [
    path('', views.quote_req, name = 'quote-request'),
]