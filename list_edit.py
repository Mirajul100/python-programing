todos = []

while True:
    userInput = input("Enter add , show , exit , edit : ")

    match userInput.lower():
        case "add":
            todo = input ("Enter the value you need to add : ")
            todos.append(todo.title())
        case "show":
            for index , item in enumerate(todos):
                print (f"{index +1} Name:{item}")
        case "exit":
            break
        case "edit":
            number = int(input ("Enter the number you need to edit the value : "))
            number = number - 1
            newTodos = input ("Enter the value : ")
            todos[number] = newTodos
        case default:
            print ("You entered the wrong value!")

print ("End the program thank you")

