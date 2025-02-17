File = "file/employ.txt"
while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    if "add" in user_input.lower():
        Employ = user_input[4:] + "\n"

        with open (f"{File}" , "r") as file:
            employ = file.readlines()

        employ.append(Employ)

        with open (f"{File}" , "w") as file :
            file.writelines(employ)

    elif "show" in user_input.lower():
        with open (f"{File}" , "r") as file:
            employ = file.readlines()

        for index , item in enumerate(employ):
            print (f"{index + 1}. {item.title().strip("\n")}")

    elif "exit" in user_input.lower():
        break

    elif "edit" in user_input.lower():

        number = int (input ("Enter the number you need to edit : "))
        number -= 1

        newEmploy = input ("Enter the name you need to edit : ")

        with open(f"{File}" , "r") as file:
            employ = file.readlines()

        print (f"You edited : {employ[number].title().strip()}--TO--{newEmploy.title()}")
        
        employ[number] = newEmploy + "\n"

        with open (f"{File}" , "w") as file:
            file.writelines(employ)

    elif "delete" in user_input.lower():

        number = int (input("Enter the number you need to delete : "))
        number -= 1

        with open (f"{File}" , "r") as file:
            employ = file.readlines()

        print (f"Deleted Name is : {employ[number].title()}")
        employ.pop(number)

        with open (f"{File}" , "w") as file:
            file.writelines(employ)

    else :
        print ("Comment is not valid!")

print ("Thank you")