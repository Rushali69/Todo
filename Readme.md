📝 To-Do List Application (Console-Based)

A simple Python-based To-Do List manager 

This application allows users to add, view, and remove tasks, with all tasks saved to a text file for persistence.


---

🚀 Features

✔ Add new tasks

✔ View all tasks

✔ Remove a task by number

✔ Tasks are stored in a file (tasks.txt)

✔ Simple and user-friendly console interface

✔ Uses Python lists & file handling



---

📂 Project Structure

.
├── todo.py        # Main application file
└── tasks.txt      # Stores tasks (auto-created)


---

▶️ How to Run

1. Make sure you have Python 3 installed.


2. Download or clone the repository:

git clone

https://github.com/Rushali69/Todo.git

3. Navigate into the folder:

cd todo-app


4. Run the script:

python todo.py




---

📘 How It Works

Tasks are stored in a Python list.

The list is loaded from tasks.txt at the start.

Any changes (add/remove) are written back to the file.

This makes the to-do list persistent, even after closing the program.



---

🧠 Key Concepts Used

File Handling (open(), reading/writing files)

Lists in Python

String Manipulation (strip())

Loops & Conditionals

User input handling



---

📜 Sample Menu

===== TO-DO LIST MENU =====
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
===========================