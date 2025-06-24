

from django.contrib import admin
from django.urls import path , include

from  .views import  *
urlpatterns = [

    path('' , todos ,  name  = 'index') ,
    path('add/' ,  add_todo , name =  'add') ,
    path('update/' ,  update_todo , name  = 'update'  ) ,
    path('delete/' , delete_todo ,  name = 'delete')
]
