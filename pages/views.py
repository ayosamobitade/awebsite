from django.shortcuts import render

# Create your views here.

def pages(request):
    return render('pages/index.html')