from django.shortcuts import render, redirect
from .models import Task


def index(request):
    # Fetch all tasks from the DB
    tasks = Task.objects.all().order_by('-created_at')

    # Pass them to the template in a dictionary
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add_task_jinja(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')