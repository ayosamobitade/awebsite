from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

from .models import Quote
from .forms import QuoteForm
from django.views.generic import ListView

from pages.models import Page


class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'

    def get_context_date(self, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'quotes/quotes.html', {'form':form, 'page_list': Page.objects.all(), 'susbmitted':submitted })