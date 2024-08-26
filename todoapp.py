import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.root.minsize(600, 400)
        self.root.configure(bg="#ebdef0")

        self.task_label = tk.Label(root, text="Enter a New Task",bg="#ebdef0",font=("Helvetica", 14, "bold"),fg="#003366")
        self.task_label.pack(padx=10, pady=10)
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task,bg='#7d3c98',fg="#f8f9f9",activebackground="#6c3483")
        self.add_button.pack(pady=10)
        self.task_list = tk.Listbox(root, width=50, height=14)
        self.task_list.pack(padx=10, pady=10)

        button_frame = tk.Frame(root,bg="#ebdef0")
        button_frame.pack(padx=20,pady=20)
        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task,bg='#7d3c98',fg="#f8f9f9",activebackground="#6c3483")
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.complete_button = tk.Button(button_frame, text="Mark Complete", command=self.mark_complete,bg='#7d3c98',fg="#f8f9f9",activebackground="#6c3483")
        self.complete_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.filter_button = tk.Button(button_frame, text="Filter Tasks", command=self.filter_tasks,bg='#7d3c98',fg="#f8f9f9",activebackground="#6c3483")
        self.filter_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get().title()
        if task:
            self.tasks.append({"task": task, "complete": False})
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Alert","You Must Enter a Task.")

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.tasks.pop(selected_task[0])
            self.task_list.delete(selected_task[0])
        else:
            messagebox.showwarning("Alert","Select a task.")

    def mark_complete(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks[index]["complete"] = True
            self.task_list.delete(index)
            self.task_list.insert(index, f"{self.tasks[index]['task']} (Complete)")
        else:
            messagebox.showwarning("Alert","Select a task.")

    def filter_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task["complete"]]
        complete_tasks = [task for task in self.tasks if task["complete"]]
        self.task_list.delete(0, tk.END)
        for task in incomplete_tasks:
            self.task_list.insert(tk.END, task["task"])
        for task in complete_tasks:
            self.task_list.insert(tk.END, f"{task['task']} (Complete)")

    def run(self):
        self.root.mainloop()

root = tk.Tk()
root.title("To-Do List App")
app = ToDoListApp(root)
app.run()