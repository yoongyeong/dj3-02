from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin, get_attachment_model
from .models import Product, Cluster


class ProductAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'is_published',
                    'is_promo', 'cluster', 'is_on_slide')
    list_display_links = ('id', 'name')
    list_filter = ('cluster',)
    list_editable = ('is_published', 'is_promo', 'is_on_slide')
    search_fields = ('name',)
    summernote_fields = 'features'


admin.site.register(Product, ProductAdmin)
admin.site.register(Cluster)


admin.site.unregister(get_attachment_model())
