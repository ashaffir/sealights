from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("note-post/", views.NotePostAPIView.as_view(), name="note-post"),
    path("note-read/", views.NoteReadAPIView.as_view(), name="note-read"),
]
