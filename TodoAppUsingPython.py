#Todo App
# Declaration of four functions to handle  the todo app
todo_list = []
def AddItems():
   
    item = input("Enter the item to add: ")
    todo_list.append(item)
def PrintItems():
    if not todo_list:
        print("No items in the list.")
    else:
        print("Todo List:")
        for item in todo_list:
            print(f"- {item}")
def DeleteItems():
    if not todo_list:
        print("No items to delete.")
    else:
        item = input("Enter the item to delete: ")
        if item in todo_list:
            todo_list.remove(item)
            print(f"Item '{item}' deleted from the list.")
        else:
            print(f"Item '{item}' not found in the list.")
    
def ClearItems():
        todo_list.clear()
        print("All items cleared from the list.")



while True:
    print("!-----------------Welcome to my Todo App ------------------------!")
    print("1. To Add  the itmes:")
    print("2. To Print The Items:")
    print("3. To Delete The Items:")
    print("4. To Clear The Items Inside The Todo Apps:")
    print("5. To Exit From The Apps")
    num=input("Enter the choice: ")
    if(num=='5'):
        print("Existing the Apps , Thank you to use my apps:")
        break
    elif(num=='1'):
        AddItems()
    elif(num=='2'):
        PrintItems()
    elif(num=='3'):
        DeleteItems()
    elif(num=='4'):
        ClearItems()
        
    else:
        print("Sorry you are entering wrong choice ! Try again ")
