from django.shortcuts import render

# Create your views here.
from .models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }
    return render(request, 'pages/page.html', context)