
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
# Create your views here.
import json

def DetailUser(request):
    if request.method =="POST":
        post_data = json.loads(request.body)
        if post_data["username"] and post_data["password"]:
            try :
                User.objects.get(full_name=post_data["username"])
                return HttpResponse("User was existed")
            except :
                User.objects.create(full_name=post_data["username"],password=post_data["password"])
                return HttpResponse("created user")

def DeleteUser(request):
    if request.method == "DELETE":
        user_id = request.GET['user_id']
        delete_data = json.loads(user_id)
        print(delete_data)
        return HttpResponse("deleted")

def LoginUser(request):
    pass
