from django.contrib import admin
from django.urls import path, include

from pages.views import index, about, contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('contact/', contact),
]