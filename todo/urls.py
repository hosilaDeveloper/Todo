from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('todo_list/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('update/<int:todo_id>/', todo_edit, name='todo_edit'),
    path('delete/<int:todo_id>/', todo_delete, name='todo_delete'),
]
