from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView,DetailView
from dictionary.models import Letter,Page

IMAGE_URL_PATH = "https://storage.googleapis.com/dictionary-nearline/images/page_"

class IndexView(ListView):
    model = Letter
    template_name = 'base.html'
    context_object_name = 'letters'

class PageView(DetailView):
    model = Page
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page = kwargs['object']
        file_name = "%02d/%02d_original.png" % (page.number,page.number)
        
        context['letters'] = Letter.objects.all()
        context['pages'] = Page.objects.filter(letter_id=page.letter_id)
        context['page_url'] = IMAGE_URL_PATH + file_name
        
        return context