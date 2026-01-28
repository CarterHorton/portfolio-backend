from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the index page for projects")

def projects_journals(request, projectEntry_id):
    return HttpResponse("This is the project list page for certian journals for: %s" % projectEntry_id)

# This page won't actually exist btw its just for testing purposes
def journal(request, journalEntry_id):
    return HttpResponse("This is the journal page for entry: %s" % journalEntry_id)
