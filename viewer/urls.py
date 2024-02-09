from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:file_id>/", views.file_view, name="file view"),
]
