from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.contrib.auth.decorators import login_required



def index(request):
    tasks = Task.objects.all()  # pylint: disable=no-member
    return render(request, 'todo/index.html', {'tasks': tasks})


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todo/detail.html', {'task': task})


@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(# pylint: disable=no-member
            user=request.user, 
            title=title,
            description=description
        )
        return redirect('index')
    return render(request, 'todo/create_task.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'todo/update_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'todo/delete_task.html', {'task': task})


