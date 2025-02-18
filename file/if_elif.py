File = "file/employ.txt"
while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    if user_input.lower().startswith("add"):
        Employ = user_input[4:] + "\n"

        with open (f"{File}" , "r") as file:
            employ = file.readlines()

        employ.append(Employ)

        with open (f"{File}" , "w") as file :
            file.writelines(employ)

    elif user_input.lower().startswith("show"):
        with open (f"{File}" , "r") as file:
            employ = file.readlines()

        for index , item in enumerate(employ):
            print (f"{index + 1}. {item.title().strip("\n")}")

    elif user_input.lower().startswith("exit"):
        break

    elif user_input.lower().startswith("edit"):
        try:
            number = int (user_input[5:])
            number -= 1

            newEmploy = input ("Enter the name you need to edit : ")

            with open(f"{File}" , "r") as file:
                employ = file.readlines()

            print (f"You edited : {employ[number].title().strip()}--TO--{newEmploy.title()}")
            
            employ[number] = newEmploy + "\n"

            with open (f"{File}" , "w") as file:
                file.writelines(employ)
        except ValueError:
            print ("You entered wrong please enter number")
            continue

    elif user_input.lower().startswith("delete"):
        try:

            number = int (user_input[7:])
            number -= 1

            with open (f"{File}" , "r") as file:
                employ = file.readlines()

            print (f"Deleted Name is : {employ[number].title()}")
            employ.pop(number)

            with open (f"{File}" , "w") as file:
                file.writelines(employ)
        except ValueError:
            print ("Enter the number to delete the name")
            continue

    else :
        print ("Comment is not valid!")

print ("Thank you")