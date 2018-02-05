from django.contrib import admin
from dictionary.models import Page,Letter,Section
# Register your models here.
  
class PageAdmin(admin.ModelAdmin):
  search_fields = ['number']
  ordering = ('number',)
admin.site.register(Page, PageAdmin)

class LetterAdmin(admin.ModelAdmin):  
  ordering = ('sort_order',)
admin.site.register(Letter, LetterAdmin)

class SectionAdmin(admin.ModelAdmin):  
  ordering = ('sort_order',)
admin.site.register(Section, SectionAdmin)