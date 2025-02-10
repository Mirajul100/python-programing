values = []

while True :
    user_input = input ("Enter add , show , exit : ")
    user_input = user_input.strip()

    match user_input.lower():
        case "add" :
            value = input("Enter the value : ")
            values.append(value.capitalize())
        case "show":
            for trop in values:
                # trop = trop.title()
                print (trop.title())
        case "exit":
            break
        case unknown:
            print ("You print wrong value")

print("Program is ended")

