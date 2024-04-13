 # Create your views here.
# {
#     "count" : 3 ,
#     "detail" :
#     [
#     {
#         "full_name":"admin1",
#         "task":["don nha","rua bat"]
#     },
#     {
#         "full_name":"admin2",
#         "task":["giat quan ao","chay bo"]
#     }
#     ]
# }
dict_result = {}
dict_result["count"] = 3
dict_result["detail"] = []

users_with_tasks = [('admin', 'tap the duc'), ('admin', 'danh rang'),
                    ('admin', 'giat quan ao'), ('admin', 'suc mieng'), ('admin1', 'tap the duc'),
                    ('admin2', None)]

# Loop through each user
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

print(dict_result)
