from os.path import exists


def show_list(todo_list):
    """Display tasks with current status"""
    print("\nCurrent ToDo List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")


def mark_completed(todo_list):
    """Handle task completion marking"""
    try:
        mark_task = int(input("Enter Task Number To Mark 🟢: "))
        if 1 <= mark_task <= len(todo_list):
            old_task = todo_list[mark_task - 1]

            # Prevent duplicate [Done] tags
            if "[Done]" not in old_task:
                marked_task = f"{old_task.strip()} [Done]"
                todo_list[mark_task - 1] = marked_task
                print(f"Marked: {old_task} → {marked_task}")
            else:
                print("Task already marked as done!")
        else:
            print(f"Invalid number (1-{len(todo_list)} only)")
    except ValueError:
        print("Invalid input! Numbers only please.")


def edit_task(todo_list):
    """Handle task editing functionality"""
    try:
        edit_task_num = int(input("Enter Task Number To Edit 📝: "))
        if 1 <= edit_task_num <= len(todo_list):
            old_task = todo_list[edit_task_num - 1]
            new_task = input("Enter new task: ").strip()
            if new_task:
                todo_list[edit_task_num - 1] = new_task
                print(f"Updated: {old_task} → {new_task}")
            else:
                print("Task not updated - empty input!")
        else:
            print(f"Invalid number (1-{len(todo_list)} only)")
    except ValueError:
        print("Invalid input! Numbers only please.")


def task_management():
    ToDo_list = []
    while True:
        print("\n" + "-" * 40)
        print(''' [1] ADD 🟢 \n [2] DELETE ❌ \n [3] TASK STATUS 📝\n [4] SHOW 📃\n [5] Load/Edit File\n [6] EXIT ⛔''')
        user_choice = input("Please choose from 1-6: ").strip()

        # [1] ADD TASK
        if user_choice == '1':
            add_task = input("Enter ToDo Task: ").strip()
            if add_task:
                ToDo_list.append(add_task)
                print(f"Task [{add_task}] added ✅")
            else:
                print("Empty task not allowed!")

        # [2] DELETE TASK
        elif user_choice == "2":
            if not ToDo_list:
                print("Your list is empty!")
                continue
            show_list(ToDo_list)
            try:
                delete_task = int(input("Enter Task Number To DELETE: "))
                if 1 <= delete_task <= len(ToDo_list):
                    removed = ToDo_list.pop(delete_task - 1)
                    print(f"Task Deleted [{removed}] ❌")
                else:
                    print(f"Invalid number (1-{len(ToDo_list)} only)")
            except ValueError:
                print("Numbers only please!")

        # [3] TASK STATUS (Mark/Edit)
        elif user_choice == "3":
            if not ToDo_list:
                print("Your list is empty!")
                continue

            show_list(ToDo_list)
            print("\nTask Operations:")
            print("  [1] Mark Complete\n  [2] Edit Task")
            action = input("Choose operation (1-2): ").strip()

            if action == "1":
                mark_completed(ToDo_list)
            elif action == "2":
                edit_task(ToDo_list)
            else:
                print("Invalid operation choice!")

        # [4] SHOW LIST
        elif user_choice == "4":
            if ToDo_list:
                show_list(ToDo_list)
            else:
                print("Your list is empty!")

        # [5] FILE OPERATIONS
        elif user_choice == "5":
            filename = input("Enter filename (e.g., mylist): ").strip()
            if not filename.endswith('.txt'):
                filename += '.txt'

            if exists(filename):
                ToDo_list.clear()
                with open(filename, 'r') as file:
                    ToDo_list.extend(line.strip() for line in file if line.strip())

                if ToDo_list:
                    show_list(ToDo_list)
                    edit_choice = input("Edit loaded list? (y/n): ").lower()
                    if edit_choice == 'y':
                        print("\nFile Operations:")
                        print("  [1] Mark Complete\n  [2] Edit Task")
                        file_action = input("Choose operation (1-2): ").strip()

                        if file_action == "1":
                            mark_completed(ToDo_list)
                            # Save changes to file after marking
                            with open(filename, 'w') as f:
                                f.write('\n'.join(ToDo_list))
                        elif file_action == "2":
                            edit_task(ToDo_list)
                            # Save changes to file after editing
                            with open(filename, 'w') as f:
                                f.write('\n'.join(ToDo_list))
                        else:
                            print("Invalid operation choice!")
                else:
                    print("Loaded file is empty!")
            else:
                print(f"File '{filename}' not found!")

        # [6] EXIT PROGRAM
        elif user_choice == "6":
            if ToDo_list:
                show_list(ToDo_list)
                filename = input("Save as (leave empty to skip): ").strip()
                if filename:
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    with open(filename, 'w') as f:
                        f.write('\n'.join(ToDo_list))
                    print(f"Saved as {filename}")
            print("\nHave a Good Day ♥")
            break

        else:
            print("Invalid choice. Please select 1-6.")


task_management()