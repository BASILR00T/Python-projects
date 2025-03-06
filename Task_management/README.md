# Python Todo List Manager

A command-line task management system with file persistence and interactive features.

## 📝 Description

This CLI tool helps you manage tasks with:
- Add/Delete/Edit operations
- Task completion marking
- File-based saving/loading
- Interactive menus with emoji indicators

## ✨ Key Features

- **CRUD Operations**: Create, Read, Update, Delete tasks
- **Task Status**: Mark tasks as completed with `[Done]` tags
- **File Management**: Save/Load lists to `.txt` files
- **Input Validation**: Error handling for invalid inputs
- **Cross-Platform**: Works on Windows/macOS/Linux

## 🚀 Usage
Run the program:
```python task_management.py```


## Menu Options:
Key Action Description
````
1. Add Task 🟢	Add new task to list

2. Delete Task ❌ Remove task by number

3. Task Status 📝 Mark complete/Edit task

4. Show List 📃	Display current tasks

5. Load/Edit File Import from/save to text files

6. Exit ⛔ Save & quit program
````
## File Operations
* Save Format: Plain text (1 task per line)

* Auto-save: Changes to loaded files are saved automatically

* Naming: .txt extension added automatically

📋 Examples
````
* Add & Mark Task
[1] ADD 🟢
Enter ToDo Task: Buy groceries

* Task [Buy groceries] added ✅

[3] TASK STATUS 📝

Choose operation (1-2): 1

Enter Task Number To Mark 🟢: 1

Marked: Buy groceries → Buy groceries [Done]


## Load & Edit File

[5] Load/Edit File
Enter filename: shopping

Loaded File Contents:
1. Milk [Done]
2. Eggs

* Edit task 2:

New task: Organic eggs

Updated: Eggs → Organic eggs

Changes saved to shopping.txt
````
## 🛠️ Common Issues
1. File Not Found:
* Ensure files are in same directory
* Use exact filename (case-sensitive)

2. Empty Lists:
* Prevent accidental deletion with confirmation prompts