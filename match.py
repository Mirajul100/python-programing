values = []

while True :
    user_input = input ("Enter add , show , exit : ")
    user_input = user_input.strip()

    match user_input:
        case "add" :
            value = input("Enter the value : ")
            values.append(value.capitalize())
        case "show":
            for trop in values:
                print (trop)
        case "exit":
            break

print("Program is ended")

