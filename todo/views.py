from django.shortcuts import render
from todo.models import TaskModel



def task_list(request):
    tasks = TaskModel.objects.all() 
    return render(request,'todo/Task_list.html',context={'tasks':tasks})

def task_create(request):
    return render(request,'todo/Task_create.html',context={})