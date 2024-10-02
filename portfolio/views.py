import django.db
from django.shortcuts import get_object_or_404, render
from MyProject.models import Project

def index(request):
    return render(request, 'Frontend/index.html')
def about(request):
    return render(request, 'Frontend/about.html')
def services(request):
    return render(request, 'Frontend/services.html')
def skill(request):
    return render(request, 'Frontend/skill.html')


def projects_view(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    # Check if there are no projects and add a default project
    if not projects:
        projects = [
            {
                'title': 'Default Project Title',
                'description': 'This is a dummy project description. Please add real projects from the admin panel.',
                'image': 'https://via.placeholder.com/150',  # Default image URL
                'link': '#'
            }
        ]
    return render(request, 'Frontend/project.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'frontend/project_detail.html', {'project': project})