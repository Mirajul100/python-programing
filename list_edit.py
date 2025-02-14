todos = []

while True:
    user_input = input("Enter add , show , edit , exit : ")

    match user_input:
        case "add":
            todo = input ("Enter the value : ")
            todos.append(todo)
        case "show":
            for item in todos:
                print (item.title())
        case "edit":
            number = int (input ("Enter the number you need to edit the list :"))
            number = number - 1
            value = input ("Enter the value :")
            todos[number] = value
        case "exit":
            break
        case default:
            print ("You entered the wrong value")

print ("Program is finished")