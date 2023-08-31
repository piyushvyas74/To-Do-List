import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=60)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            if task_index < len(self.tasks):
                self.tasks.pop(task_index)
                self.task_listbox.delete(task_index)
            else:
                messagebox.showwarning("Warning", "Invalid task selection.")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark complete.")
            
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            if task_index < len(self.tasks):
                self.tasks.pop(task_index)
                self.task_listbox.delete(task_index)
            else:
                messagebox.showwarning("Warning", "Invalid task selection.")
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            if task_index < len(self.tasks):
                new_task = askstring("Edit Task", "Edit the task:", initialvalue=self.tasks[task_index])
                if new_task:
                    self.tasks[task_index] = new_task
                    self.task_listbox.delete(task_index)
                    self.task_listbox.insert(task_index, new_task)
            else:
                messagebox.showwarning("Warning", "Invalid task selection.")
        else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
