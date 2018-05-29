# The file links urls to the views in views.py

from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index_view, name='index'),

    # path('dashboard/', views.index, name='index'),
    # path('admin/', admin.site.urls),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)