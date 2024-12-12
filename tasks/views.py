from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/task-list.html', ctx)

def task_form(request):
    if request.method == 'POST':
        tasks_title = request.POST.get('tasks_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if tasks_title and due_date and description:
            Task.objects.create(
                tasks_title=tasks_title,
                due_date=due_date,
                description=description
            )
            return redirect('tasks:list')
    return render(request, 'tasks/task-form.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    ctx = {'task': task}
    return render(request, 'tasks/task-detail.html', ctx)

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        tasks_title = request.POST.get('tasks_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')
        if tasks_title and due_date and description:
            task.tasks_title=tasks_title
            task.due_date=due_date
            task.description=description
            task.save()
            return redirect(task.get_detail_url())
    ctx = {'task': task}
    return render(request, 'tasks/task-form.html', ctx)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:list')
