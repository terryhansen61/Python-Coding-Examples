import tkinter as tk
from tkinter import messagebox

# ------------------------------
# File where tasks will be saved
# ------------------------------
TASK_FILE = "tasks.txt"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")

        # ------------------------------
        # Task Entry Field
        # ------------------------------
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # ------------------------------
        # Buttons
        # ------------------------------
        self.add_button = tk.Button(
            root, text="Add Task", width=15, command=self.add_task
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            root, text="Delete Task", width=15, command=self.delete_task
        )
        self.delete_button.pack(pady=5)

        # ------------------------------
        # Listbox to show tasks
        # ------------------------------
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Load saved tasks
        self.load_tasks()

    # ------------------------------
    # Add a new task
    # ------------------------------
    def add_task(self):
        task = self.task_entry.get().strip()

        if not task:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.save_tasks()

    # ------------------------------
    # Delete selected task
    # ------------------------------
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    # ------------------------------
    # Save tasks to file
    # ------------------------------
    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    # ------------------------------
    # Load tasks from file
    # ------------------------------
    def load_tasks(self):
        try:
            with open(TASK_FILE, "r") as file:
                for line in file:
                    self.task_listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass  # No saved tasks yet


# ------------------------------
# Start the application
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
