
#! TO-DO LIST CREATED USING PYTHON

print()
print("----YOUR ONE AND ONLY GO-TO TO-DO LIST----")
print()
size = int(input("Enter your total number of tasks: \n").strip())  

task = []
date = []

for i in range(size):
    work = input(f"Enter task {i+1}: ").strip() 
    time = input(f"Enter due date for task {i+1}: ").strip()   

    task.append(work)
    date.append(time)

print("\n----TO-DO LIST----")
for i in range(len(task)): 
    print(f"{i+1}. Task: {task[i]} | Due Date: {date[i]}")

print()

print("If you want to do any operations from the following just press the button corresponding to the number.")
print("1. Delete a task \n2. Edit a task \n3. Add a task \n4. Mark completed \n5. View tasks \n6. View completed tasks \n7. Exit")


completed_task = []
completed_date = []

running = True

while running:

    print()
    operate = int(input("ENTER YOUR OPERATION: "))
    print()

    match operate:
        case 1:

            deltask = int(input("Enter the task to delete: ")) - 1

            if deltask >= 0 and deltask < size:
                task.pop(deltask)  
                date.pop(deltask) 
                size -= 1
                print("Task removed successfully!")
            else:
                print("Invalid task number.")

        case 2:

            edit = int(input("Enter the task you want to edit: ")) - 1 

            if (edit >= 0 and edit < size):
                task[edit] = input("Enter new task: ")
                date[edit] = input("Enter new due date: ")

                print("Task updated successfully!")
            else:
                print("Invalid task number.")

        case 3:

            new_task_add = input("Enter the new task: ").strip()
            new_date_add = input("Enter the due date for the new task: ").strip()

            task.append(new_task_add)  
            date.append(new_date_add)   
            size += 1  

            print("Task added successfully!")

        case 4:

            completeIndex = int(input("Enter the task number which is completed: ")) - 1

            if (completeIndex >= 0 and completeIndex < size):
                completed_task.append(task[completeIndex])
                completed_date.append(date[completeIndex])

                print(f"Task Completed: {task[completeIndex]} | Due Date: {date[completeIndex]}")

                task.pop(completeIndex)  
                date.pop(completeIndex)  
                size -= 1
            else:
                print("Invalid task number.")

        case 5: 
            print("----TO-DO LIST----")
            for i in range(len(task)):
                print(f"{i+1}. Task: {task[i]} | Due Date: {date[i]}")

        case 6:
            print("----COMPLETED TASKS----")
            for i in range(len(completed_task)):
                print(f"{i+1}. Task: {completed_task[i]} | Due Date: {completed_date[i]}")

        case 7:
            running = False
            print("Exiting...")
            print("Done!")

        case _:
            print("Invalid Input. Try again.")

print("================================")
