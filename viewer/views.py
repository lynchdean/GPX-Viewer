from django.http import Http404
from django.shortcuts import render

from .models import File

def index(request):
    file_list = File.objects.order_by("title")
    context = {"file_list": file_list}
    return render(request, "viewer/index.html", context)

def file_view(request, file_id):
    try:
        file = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        raise Http404("File does not exist")
    return render(request, "viewer/file.html", {"file":file})