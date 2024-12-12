from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='list'),
    path('create/', views.task_form, name='create'),
    path('detail/<int:pk>/', views.task_detail, name='detail'),
    path('update/<int:pk>/', views.task_update, name='update'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]