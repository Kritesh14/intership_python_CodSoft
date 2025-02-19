# intership_python_CodSoft
"This repository contains projects developed as part of the CodSoft Python Programming Internship. Each project is designed to enhance my Python skills and problem-solving abilities. Below are the tasks included in this repository:"  Task 1: To-Do List Application Task 2: Calculator Task 3: Password Generator


Task 1: To-Do List Application Task Code
def task():
    tasks = []  # Empty list to store tasks
    print("--- Task To-Do List ---")
    
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(total_task):  # Corrected loop range
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append(task_name)
        
    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("\nEnter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added.")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            if update_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Task updated to '{up}'.")
            else:
                print(f"Task '{update_val}' not found.")

        elif operation == 3:
            del_val = input("Which task do you want to delete? ")
            if del_val in tasks:
                tasks.remove(del_val)  # `remove()` is better than `del tasks[ind]`
                print(f"Task '{del_val}' has been deleted.")
            else:
                print(f"Task '{del_val}' not found.")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid operation. Please enter a number between 1 and 5.")

# Call the function
task()
