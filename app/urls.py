from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:id>/', views.update_todo, name='update_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
]
