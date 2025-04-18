
from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('todos/', all_todos, name='all_todos'),
    path('todos/add/', add_todo, name='add_todo'),
    path('todos/<int:todo_id>/edit/', edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('toggle_todo_completion/<int:todo_id>/', toggle_todo_completion, name='toggle_todo_completion'),
]