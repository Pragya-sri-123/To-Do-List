import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App with Checkboxes")
        self.root.geometry("400x400")

        # Initialize task list and checkboxes list
        self.tasks = []
        self.checkboxes = []

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Task Entry Box
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_frame = tk.Frame(self.root)
        self.task_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for update and delete
        self.update_button = tk.Button(self.root, text="Update Task", width=20, command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description != "":
            task_index = len(self.tasks)
            self.tasks.append({'description': task_description, 'status': False})  # False indicates not checked (pending)
            self.add_task_to_gui(task_index)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def add_task_to_gui(self, task_index):
        # Create a checkbox for the new task
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.task_frame, text=self.tasks[task_index]['description'], variable=checkbox_var, command=lambda idx=task_index: self.toggle_task_status(idx, checkbox_var))
        checkbox.grid(row=task_index, column=0, sticky="w", padx=10)
        self.checkboxes.append(checkbox_var)

    def toggle_task_status(self, task_index, checkbox_var):
        # Update task status (checked or unchecked)
        self.tasks[task_index]['status'] = checkbox_var.get()

    def update_task(self):
        try:
            selected_task_index = self.get_selected_task_index()
            new_description = self.task_entry.get()

            if new_description != "":
                self.tasks[selected_task_index]['description'] = new_description
                self.update_task_in_gui(selected_task_index)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new description.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def update_task_in_gui(self, task_index):
        # Update the task description in the GUI
        for widget in self.task_frame.winfo_children():
            widget.destroy()  # Clear previous checkboxes and labels
        self.checkboxes.clear()  # Clear the checkbox list
        for idx, task in enumerate(self.tasks):
            self.add_task_to_gui(idx)

    def delete_task(self):
        try:
            selected_task_index = self.get_selected_task_index()
            self.tasks.pop(selected_task_index)
            self.update_task_in_gui(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def get_selected_task_index(self):
        # Get the index of the task selected (based on the checkbox index)
        for idx, checkbox_var in enumerate(self.checkboxes):
            if checkbox_var.get():
                return idx
        raise IndexError("No task selected.")

# Create the main window
root = tk.Tk()

# Initialize the TodoApp
app = TodoApp(root)

# Run the application
root.mainloop()
