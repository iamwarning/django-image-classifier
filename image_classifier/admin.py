from django.contrib import admin
from .models import Image

# Register your models here.
# admin.site.register(Image)
admin.site.site_header = 'Image Classifier'
admin.site.index_title = 'Control Panel'
admin.site.site_title = 'Image Classifier'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    icon_name = 'image'
    list_display = ('picture', 'classified', 'uploaded')
    list_filter = ['classified']
    search_fields = ('uploaded', 'classified')
    ordering = ('-uploaded',)