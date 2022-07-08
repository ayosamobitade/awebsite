from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

from .models import Quote
from .forms import QuoteForm