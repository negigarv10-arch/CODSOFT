# The main list where all your tasks will be stored.
# Each item in the list will be a dictionary containing the task details.
todo_list = []
def add_task():
    """Prompts the user for a new task and adds it to the list."""
    task_name = input("Enter the task you want to add: ")
    # Create a dictionary for the new task
    new_task = {
        'name': task_name,
        'status': 'Pending' # All new tasks start as 'Pending'
    }
    todo_list.append(new_task)
    print(f"\n✅ Task '{task_name}' added successfully!")

def view_tasks():
    """Displays the current list of tasks with their status."""
    if not todo_list:
        print("\nYour To-Do list is currently empty!")
        return
    
    print("\n--- YOUR TO-DO LIST ---")
    # Loop through the list to display each task
    # enumerate() gives you both the index (i) and the item (task)
    for i, task in enumerate(todo_list):
        # Task numbers start from 1 for the user (i + 1)
        task_number = i + 1
        name = task['name']
        status = task['status']
        
        # Display the task clearly with its status
        print(f"{task_number}. [{status:^9}] {name}")
    print("-----------------------")

def mark_complete():
    """Allows the user to mark a task as 'Complete'."""
    if not todo_list:
        print("\nCannot mark complete. The list is empty.")
        return

    # First, show the user the tasks so they can choose
    view_tasks()
    
    try:
        # Get the task number from the user
        task_to_complete = int(input("Enter the NUMBER of the task to mark as COMPLETE: "))
        
        # Adjust the number to the correct list index (number - 1)
        index = task_to_complete - 1
        
        # Check if the entered index is valid
        if 0 <= index < len(todo_list):
            # Update the status of the chosen task
            todo_list[index]['status'] = 'Complete'
            task_name = todo_list[index]['name']
            print(f"\n🎉 Task '{task_name}' marked as COMPLETE!")
        else:
            print("\n❌ Error: Invalid task number.")
            
    except ValueError:
        # Handle cases where the user enters text instead of a number
        print("\n❌ Error: Please enter a valid number.")

def main():
    """The main function that runs the application loop."""
    print("Welcome to your Python To-Do List Application!")
    
    while True:
        # Display the main menu options
        print("\n--- Main Menu ---")
        print("1. Add a new Task")
        print("2. View all Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit Application")
        print("-----------------")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            print("\nThank you for using the To-Do List. Goodbye!")
            break # Exits the while loop, ending the program
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

# Standard Python entry point: ensures the 'main' function runs when the script starts.
if __name__ == "__main__":
    main()