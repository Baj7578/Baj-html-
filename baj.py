#1 -add tasks to a list
#2 -mark task as complete
#3 -view tasks
#4 -Quit

def add_task():
   #get tasks from user
     task = input("Enter task:")
   #define tasks status
     task_info = {"task":task,"completed":False}
   #add task to the list of task
     tasks.append (task_info)
     print("task added to the list successfuly")
def mark_task_complete():
   #get list incomplete tasks
     incomplete_tasks = [task for task in tasks if task["completed"]==False]
     if not incomplete_tasks:
        print("no tasks the mark as complete")

   #show them to the user
     for i,task in enumerate(incomplete_tasks):

       print(f"{i+1}-{task['task']}")
       print("-"*30)
   #get the task from the user
     task_number = int(input("choos the taskto complete:"))
   #mark the task es completed
     incomplete_tasks[task_number - 1]["completed"] = True
   #aliasing

   #print a message to the user
     print("task marked completed")
def view_tasks():
  if not tasks:
      print("no tasks to view")
      return 
  for i,task in enumerate(tasks):
#if task("completed"):
   #status = "✔️"
   #else:
   #status = "❌️"
      status = "✔️" if task["completed"] else"❌️"
      print(f'{i+1}. {task["task"]}{status}')

message = """1 -add tasks to a list
2 -mark task as complete
3 -view tasks
4 -Quit"""
tasks = []
while True:
    print (message)
    choice = input("Enter your choice:")
    if choice =="1":
      add_task()
    elif choice =="2":
      mark_task_complete()
    elif choice =="3":
      view_tasks()
    elif choice =="4":
       break
    else:
     print ("invalid choice , please enter task")