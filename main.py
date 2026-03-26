from todo import add_task, list_tasks

add_task("Initial task by A")

tasks = list_tasks()
for t in tasks:
    print(t)
    
    add_task("B: buy groceries")
    
    
remove_last_task()
add_task("B: replaced last task")
add_task("B: buy groceries")