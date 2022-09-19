from xml.dom.minidom import Document
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# from .models import upload_book
from django.http import HttpRequest, HttpResponse
from django.shortcuts import HttpResponse, render

from .models import FilesUpload

# from Trading_Project import MainApp
def home(request):
    if request.method =="POST":
        file2=request.FILES["files"]
        Document=FilesUpload.objects.create(file=file2)
        Document.save()
    return render(request,"index.html")


def review(request):
    return HttpResponse("file is submitted")