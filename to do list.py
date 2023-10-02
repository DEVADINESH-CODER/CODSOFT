alltasks = []

#showing  tasks
def display_tasks():
    if alltasks==[]:
        print("You have no tasks in your TO-DO list.")
    else:
        print("Your TO-DO list:")
        for i, task in enumerate(alltasks, start=1):
            print(f"{i}. {task}")

#add a task to the TO-DOlist
def add_task(task):
    alltasks.append(task)
    print("Added:",task)

#REMOVE THE COMPLETED TASK
def completed_task(task_number):
    if 1 <= task_number <= len(alltasks):
        deleted_task = alltasks.pop(task_number - 1)
        print("Completed:",deleted_task)
    else:
        print("Invalid task number.")

# MAIN PAGE...................................
while True:
    print("\nOptions:")
    print("1. Display TO-DO list")
    print("2. Add a task")
    print("3. Completed task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        display_tasks()
        task_number = int(input("Enter the task number that you have completed: "))
        completed_task(task_number)
        print("REMAINING TASKS:")
        display_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
