from django.shortcuts import render, redirect

# Create your views here.

data  = {

}


def todos(request) :
    context  =  {'data' :  data.items()}
    return render(request ,'index.html'  , context )

def add_todo(request) :
    if request.method  == 'POST' :
        index  =  len(data) +1
        todo  =  request.POST.get('todo')
        data[index] =  todo
        return  redirect('index')


def update_todo(request  , id) :
    if request.method == "POST" :
        todo  =  request.POST.get('todo')
        data[id] =  todo
        return  redirect('index')


def  delete_todo(request , id) :
        del  data[id]
        return redirect('index')