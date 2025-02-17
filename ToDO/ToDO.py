def todo_function(): #create a function For the script logic
    ToDoList = [] #define a variable / list to store data
    while True:
            usertInput = str(input("Enter what you want to do (or type 'quit' to finish):")) #get Userinput
            if usertInput.lower() == "quit":
                if not ToDoList:  # Check if the list is empty
                    print("Your ToDoList is empty. Goodbye!")
                    break
                listname = str(input("PLS name your list: "))
                with open(f"{listname}.txt", "w") as save_file:  # Use 'with' statement to handle file
                    newline = "\n".join(ToDoList)
                    save_file.write(newline)
                print(f"{listname}:↴\n{newline} \n___________________\n See u next time 💙") #print the list
                break
            else:
                ToDoList.append(f"{usertInput} [ ]") # add/write the userinput to "ToDoList"




todo_function()
