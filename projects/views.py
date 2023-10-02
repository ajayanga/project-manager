from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.
def projectList(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/projects.html', context)


def projectDetail(request, pk):
    project = get_object_or_404(Project, id=pk)
    project_tasks = project.task_set.all()
    context = {'project':project, 'project_tasks':project_tasks}
    return render(request, 'projects/project-detail.html', context)
