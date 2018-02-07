from bakery.views import BuildableListView,BuildableDetailView
from dictionary.models import Letter,Page

IMAGE_URL_PATH = "/static/dictionary/pages/"

class IndexView(BuildableListView):
    model = Letter
    template_name = 'base.html'
    context_object_name = 'letters'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_url'] = IMAGE_URL_PATH + "000_title.png"

        return context

class PageView(BuildableDetailView):
    model = Page
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page = kwargs['object']
        file_name = "%03d_original.png" % (page.number,)
        
        context['letters'] = Letter.objects.all()
        context['pages'] = Page.objects.filter(letter_id=page.letter_id)
        context['current_page'] = page
        context['page_url'] = IMAGE_URL_PATH + file_name
        
        return context