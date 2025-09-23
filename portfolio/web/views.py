

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.filter(is_published=True).order_by('order', '-created_at')
    return render(request, "web/index.html", {"projects": projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "web/project_detail.html", {"project": project})
