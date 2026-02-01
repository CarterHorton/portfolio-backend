from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import projectEntry

# Create your views here.
def index(request):
    allProjects = projectEntry.objects.all()
    template = loader.get_template("journals/index.html")
    context = {'latest_projectEntry_list': allProjects}
    return HttpResponse(template.render(context, request))

def projects_journals(request, projectEntry_id):
    return HttpResponse("This is the project list page for certian journals for: %s" % projectEntry_id)

