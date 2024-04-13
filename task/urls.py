from django.urls import path, include
from . import views


urlpatterns = [
    path('tasks/',views.ListOrCreateTask, name="registeruser"),
    path('tasks/<int:task_id>/', views.DetailTaskByid, name="deleteUser"),
    path('tasks/<slug:slug>/', views.DetailTaskBySlug, name="deleteUser"),
]