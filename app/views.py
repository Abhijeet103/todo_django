from django.shortcuts import render, redirect , get_object_or_404

# Create your views here.
from  . models import Todo




def todos(request) :
    all_todo = Todo.objects.all()
    context  =  {'data' :  all_todo}
    print(all_todo)
    return render(request ,'index.html'  , context )

def add_todo(request) :
    if request.method  == 'POST' :
        todo  =  request.POST.get('todo')
        todo_object  = Todo(todo  = todo)
        todo_object.save()
        return  redirect('index')


def update_todo(request  , id) :
    if request.method == "POST" :
        todo  =  request.POST.get('todo')
        todo_object  =  get_object_or_404(Todo ,  id = id)
        todo_object.todo  =   todo
        todo_object.save()
        return  redirect('index')


def  delete_todo(request , id) :
        todo  = get_object_or_404(Todo ,  id  =  id )
        todo.delete()
        return redirect('index')