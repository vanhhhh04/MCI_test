from django.urls import path, include
from . import views


urlpatterns = [
    path('users',views.DetailUser, name="registeruser"),
    path('users/delete/<int:user_id>', views.DeleteUser, name="deleteUser"),
    path('users/login', views.LoginUser, name="loginuser"),
]