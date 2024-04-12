from django.shortcuts import render, redirect, get_list_or_404
from todo.models import TaskModel
from todo.forms import TaskForm
from django.urls import reverse
from django.http import HttpResponeNotFound

def task_list(request):
    tasks = TaskModel.objects.all() 
    if search_q := request.GET.get("q"):
        #  task = task.filter(title=search_q )
        task = task.filter(title__icontains=search_q )


    return render(request,'todo/Task_list.html',context={'tasks':tasks})

def task_create(request):
    form = TaskForm()
    if request.method =="GET":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # TaskModel.objects.create(title =form.changed_data['title'],
            #                           description=form.changed_data['description'])
            return redirect(reverse("todo:task_list"))
    return render(request,'todo/Task_create.html',context={'form':form})
    
    # if request.method =="POST":
    #     form = TaskForm()
    #     return render(request,'todo/Task_create.html',context={'form':form})



def task_delete(request, task_id):
    task = get_list_or_404(TaskModel,id=task_id)
    if task :
            task.delete()
    else:
            return HttpResponeNotFound()    
    return redirect(reverse("todo:task_list"))
    

def task_edit(request, task_id):
    task = get_list_or_404(TaskModel,id=task_id)
    form = TaskForm(instatnce=task)
    if request.method =="POST":
        form = TaskForm(data=request.POST,instance=task)
        if form.is_valid():
            form.save()
        #     return redirect(reverse("todo:task_edit",kwargs={"task_id":form.instance.id}))
        # else:
            # return render(request,'todo/Task_edit.html',context={'form':form})

    return render(request,'todo/Task_edit.html',context={'form':form})




def task_done(request, task_id):
    task = get_list_or_404(TaskModel,id=task_id)
    if task :
            task.is_done = True
            task.save()
    return redirect(reverse("todo:task_list"))