class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = {
            'description': task_description,
            'status': 'pending'
        }
        self.tasks.append(task)
        print(f"Task '{task_description}' added successfully.")

    def update_task(self, task_index, new_description=None, mark_done=False):
        if 0 <= task_index < len(self.tasks):
            if new_description:
                self.tasks[task_index]['description'] = new_description
            if mark_done:
                self.tasks[task_index]['status'] = 'done'
            print(f"Task {task_index + 1} updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['description']}' deleted successfully.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task['description']} - {task['status']}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter task number to update: ")) - 1
                new_description = input("Enter new description (or leave blank to keep current): ")
                mark_done = input("Mark as done? (yes/no): ").lower() == 'yes'
                todo_list.update_task(task_index, new_description, mark_done)
            except ValueError:
                print("Invalid input, please enter a valid task number.")
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid input, please enter a valid task number.")
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
