from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'base/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'base/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'base/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'base/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'base/task_confirm_delete.html', {'task': task})
