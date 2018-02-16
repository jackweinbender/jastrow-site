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
        context['next_page'] = get_next_page(page.id)
        context['prev_page'] = get_prev_page(page.id)
        context['page_url'] = IMAGE_URL_PATH + file_name
        
        return context
    
def get_next_page(current_page):
    if is_valid_page(current_page + 1):
        return Page.objects.get(pk=current_page + 1)
    else: return Page.objects.get(pk=current_page)

def get_prev_page(current_page):
    if is_valid_page(current_page - 1):
        return Page.objects.get(pk=current_page - 1)
    else: return Page.objects.get(pk=current_page)

def is_valid_page(page_number):
    if page_number < 1: return False
    if page_number > 1705: return False
    if page_number == 684: return False
    
    return True