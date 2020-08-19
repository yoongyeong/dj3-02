from django.urls import path, include
from . import views

# Imported for Summernote in debug mode
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('summernote/', include('django_summernote.urls')),
]

# Comment these lines when NOT in debug mode (DEBUG = False)
# These lines are for Summernote
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
