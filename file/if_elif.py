from function import readFile ,writeFile

while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    if user_input.lower().startswith("add"):
        Employ = user_input[4:] + "\n"

        employName = readFile()

        employName.append(Employ)

        writeFile(employName)

    elif user_input.lower().startswith("show"):
        Employ = readFile()

        for index , item in enumerate(Employ):
            print (f"{index + 1}. {item.title().strip("\n")}")

    elif user_input.lower().startswith("exit"):
        break

    elif user_input.lower().startswith("edit"):
        try:
            number = int (user_input[5:])
            number -= 1

            newEmploy = input ("Enter the name you need to edit : ")

            Employ = readFile()

            print (f"You edited : {Employ[number].title().strip()}--TO--{newEmploy.title()}")
            
            Employ[number] = newEmploy + "\n"

            writeFile(Employ)

        except ValueError:
            print ("Enter the number you need to edit")
            continue

    elif user_input.lower().startswith("delete"):
        try:

            number = int (user_input[7:])
            number -= 1

            Employ = readFile()

            print (f"Deleted Name is : {Employ[number].title().strip("\n")}")
            Employ.pop(number)

            writeFile(Employ)

        except ValueError:
            print ("Enter the number to delete the name")
            continue

    else :
        print ("Comment is not valid!")

print ("Thank you")