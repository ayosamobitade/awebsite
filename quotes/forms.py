from django import forms
from django.forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):
    requeired_css_class = 'required'
    
    class Meta:
        model = Quote