
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from .models import User
from django.contrib import auth,messages
# Create your views here.
import json
# from django.

    

def DetailUser(request):
    if request.method =="POST":
        
        post_data = json.loads(request.body)
        if "address" not in post_data.keys():
            post_data["address"] = None 
        if "school" not in post_data.keys():
            post_data["school"] = None 

        if post_data["username"] and post_data["password"]:
            try :
                User.objects.get(full_name=post_data["username"])
                return HttpResponse("User was existed")
            except :
                print(post_data["address"])
                User.objects.create(full_name=post_data["username"],password=post_data["password"], address=post_data["address"], school=post_data["school"])
                return HttpResponse("created user")


def DeleteUser(request, user_id):
    # if user.role == '1':
    if request.method == "DELETE":
        # user = get_object_or_404(User, pk=user_id)
        # print(user.role)
        # return JsonResponse({'message':'check'})
    
        if user_id :
            User.objects.delete(pk=user_id)
    if request.method == "PUT":
        if user_id : 
            put_data = json.loads(request.body)
            if put_data["username"] and put_data["password"]:
                User.objects.update(full_name=put_data['username'], password=put_data['password'])
            else :
                return HttpResponse("you have to fill the form")


def LoginUser(request):
    # if request.user.is_authenticated: 
    #     return JsonResponse("you are already logged in!")
    if request.method == "POST":
        post_data = json.loads(request.body)
        print(post_data)
        # return HttpResponse("yes")
        if post_data["username"] is None or post_data["password"] is None:
            return HttpResponse("you have to fill in the form")
        else : 
            user = auth.authenticate(post_data['username'],password=post_data['password'])
            if user is not None :
                auth.login(request,user) 
                return HttpResponse({'message':'login success'})
            else :
                return redirect('LoginUser')
    else :
        return HttpResponse("no")