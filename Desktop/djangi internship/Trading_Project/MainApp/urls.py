from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views
from .views import home

urlpatterns = [
    
    path('',home),
    path("review",views.review )
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
