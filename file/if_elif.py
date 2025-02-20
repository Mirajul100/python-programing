def readFile(filePath):
    with open (filePath , "r") as file:
        File = file.readlines()
    return File


def writeFile(filePath , employName):
    with open (filePath , "w") as file:
        file.writelines(employName)


while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    if user_input.lower().startswith("add"):
        Employ = user_input[4:] + "\n"

        employName = readFile("file/employ.txt")

        employName.append(Employ)

        writeFile("file/employ.txt" , employName)

    elif user_input.lower().startswith("show"):
        Employ = readFile("file/employ.txt")

        for index , item in enumerate(Employ):
            print (f"{index + 1}. {item.title().strip("\n")}")

    elif user_input.lower().startswith("exit"):
        break

    elif user_input.lower().startswith("edit"):
        try:
            number = int (user_input[5:])
            number -= 1

            newEmploy = input ("Enter the name you need to edit : ")

            Employ = readFile("file/employ.txt")

            print (f"You edited : {Employ[number].title().strip()}--TO--{newEmploy.title()}")
            
            employName[number] = newEmploy + "\n"

            writeFile("file/employ.txt" , employName)

        except ValueError:
            print ("Enter the number you need to edit")
            continue

    elif user_input.lower().startswith("delete"):
        try:

            number = int (user_input[7:])
            number -= 1

            Employ = readFile("file/employ.txt")

            print (f"Deleted Name is : {Employ[number].title().strip("\n")}")
            Employ.pop(number)

            writeFile("file/employ.txt" , Employ)

        except ValueError:
            print ("Enter the number to delete the name")
            continue

    else :
        print ("Comment is not valid!")

print ("Thank you")