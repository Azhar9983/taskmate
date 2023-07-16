from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def todolist(request):
    if request.method == 'POST':
        form  = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("New task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TodoList.objects.all
        return render(request, 'todolist.html', { 'all_tasks': all_tasks } )
    
def delete_task(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == 'POST':
        task = TodoList.objects.get(pk=task_id)
        form  = TodoForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TodoList.objects.get(pk=task_id)
        return render(request, 'edit.html', { 'task_obj': task_obj } )
    
def complete_task(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def contact(request):
    context = {
        'contact_text': 'Welcome to the contact us page',
        }
    return render(request, 'contact.html', context )

def about(request):
    context = {
        'about_text': 'Welcome to the about page',
        }
    return render(request, 'about.html', context )

