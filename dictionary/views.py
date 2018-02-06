from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from dictionary.models import Letter,Page

def index(request):
    letters = Letter.objects.all()
    page = Page.objects.get(pk=1)

    page_url = "https://storage.googleapis.com/dictionary-nearline/images/"
    page_url += "page_%02d/%02d_original.png" % (page.number,page.number)

    template = loader.get_template('base.html')
    context = {
        'letters': letters,
        
    }
    
    return HttpResponse(template.render(context, request))

def page(request, page_num):
    letters = Letter.objects.all()
    page = Page.objects.get(number=page_num)

    pages = Page.objects.filter(letter_id=page.letter_id)
    
    page_url = "https://storage.googleapis.com/dictionary-nearline/images/"
    page_url += "page_%02d/%02d_original.png" % (page_num,page_num)

    template = loader.get_template('page.html')
    context = {
        'letters': letters,
        'pages': pages,
        'page_url': page_url
    }
    
    return HttpResponse(template.render(context, request))