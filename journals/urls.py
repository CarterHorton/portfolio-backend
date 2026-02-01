from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:projectEntry_id>/", views.projects_journals, name="projects_journals")
]