from django.shortcuts import render
from todo.models import TaskModel



def index(request):
    tasks = TaskModel.objects.all() 
    return render(request,'todo/Task_list.html',context={'tasks':tasks})