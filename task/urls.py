from django.urls import path, include
from . import views


urlpatterns = [
    path('tasks/',views.ListOrCreateTask, name="registeruser"),
    path('task/<int:task_id>/', views.DetailTaskByid, name="deleteUser"),
    path('task/<string:task_slug>/', views.DetailTaskBySlug, name="deleteUser"),
    path('tasks/', views.LoginUser, name="loginuser"),
]