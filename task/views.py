from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from users.models import User
import json
from django.db.models import Count


def ListOrCreateTask(request):
    if request.method == "GET":
        user_count = User.objects.aggregate(user_count=Count('id'))
        dict_result = {}
        dict_result["count"] = user_count
        dict_result["detail"] = []
        users_with_tasks = User.objects.values_list('full_name', 'task__content')
        for user in set(user_task[0] for user_task in users_with_tasks):
            dict_sub = {}
            dict_sub["full_name"] = user
            task_sub = []

            # Loop through user tasks
            for user_task in users_with_tasks:
                if user_task[0] == user:
                    # Add task to task_sub list
                    if user_task[1] is not None:
                        task_sub.append(user_task[1])

            dict_sub["task"] = task_sub
            dict_result["detail"].append(dict_sub)

        return JsonResponse(dict_result)
    if request.method == "POST":
        post_data = json.loads(request.body)
        if post_data["slug"] and post_data["content"]:
            Task.objects.create(slug=post_data["slug"], content=post_data["content"])
            return HttpResponse("Created task")
        else :
            return HttpResponse("you have to fill in the slug and content")


def DetailTaskByid(request, task_id):
    if request.method == "GET":
        task = Task.objects.get(pk=task_id)
        task_dict = {'id':task.id,
                     'content':task.content}

        print(task_dict)
        return JsonResponse(task_dict)
    if request.method == "PUT":
        try:
            task_object = Task.objects.get(pk=task_id)
            put_data = json.loads(request.body.decode('utf-8'))
            if put_data.get("slug") and put_data.get("content"):
                task_object.slug = put_data["slug"]
                task_object.content = put_data["content"]
                task_object.save()
                return HttpResponse("Updated successfully")
            else:
                return HttpResponse("You have to fill in the slug and content")
        except Task.DoesNotExist:
            return HttpResponse("ID is not valid")

    if request.method == "DELETE":
        try :
            task_object = Task.objects.get(pk=task_id)
            task_object.delete()
            return HttpResponse("deleted task")
        except :
            return HttpResponse("ID is not valid")
def DetailTaskBySlug(request, slug):
    if request.method == "GET":
        tasks = Task.objects.filter(slug__icontains=slug)

        tasks_list = []
        for task in tasks:

            task_dict = {
                'slug': task.slug,
                'content': task.content,

            }

            tasks_list.append(task_dict)

        return JsonResponse(tasks_list, safe=False)