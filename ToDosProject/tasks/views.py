from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def all_todos(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'all_todos.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Task added successfully!', extra_tags='added')
            return redirect('all_todos')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Task updated successfully!', extra_tags='updated')
            return redirect('all_todos')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.add_message(request, messages.SUCCESS, 'Task deleted successfully!', extra_tags='deleted')
    return redirect('all_todos')

def toggle_todo_completion(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    status = "completed" if todo.is_completed else "marked as incomplete"
    messages.add_message(request, messages.SUCCESS, f'Task {status}!', extra_tags='toggled')
    return redirect('all_todos')
