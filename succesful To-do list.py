import sys

print(" My todo list")
# Task = "\n1: Create New. \n2: View List. \n3: Delete. \n4: End. "
# 1print(Task)

My_Todolist = []

# A function to help add a task to the To-do list
def Create_New(task):
    My_Todolist.append(task)
    print(f"Task '{task}' added to the to-do list.")

# A function to help view the list
def View_List():
    if not My_Todolist:
        print("Your to-do list is empty.")
    else:
        print("My To-do list.")
        for i, task in enumerate(My_Todolist, 1):
            print(f"{i}. {task}")

def Delete(task):
    if task in My_Todolist:
        My_Todolist.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' file not in the to-do list.")

while True:
    Task = "\n1: Create New. \n2: View List. \n3: Delete. \n4: End. "
    print(Task)

    choice = input("\n please select what you want to do. \n Represented by their numbers: ")

    if choice == "1":
        task = input("Enter the task to add: ")
        Create_New(task)

    elif choice == "2":
        View_List()

    elif choice == "3":
        task = input("Enter to task to be delated: ")
        Delete(task)

    elif choice == "4":
        print("Thank You. \nFor Using our service. ")
        sys.exit()
    else:
        print("Invalid choice. \nRe-enter an option.")
        continue


