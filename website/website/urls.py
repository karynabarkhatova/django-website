from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from pages.views import index, about, contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contact/', contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)