from django.url import path
form . import views

urlpatterns = [
    path('', views.quote_req, name = 'quote-request'),
]