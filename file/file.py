while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    match user_input.lower():
        case "add":
            studentName = input ("Enter the student name : ") + "\n"
            
            with open("file/student_name.txt","r") as file:
                student_name = file.readlines()

            student_name.append(studentName)

            with open("file/student_name.txt","w") as file:
                file.writelines(student_name)

        case "show":
            with open("file/student_name.txt","r") as file:
                student_name = file.readlines()

            for index , item in enumerate(student_name) :
                item = item.strip("\n")
                print (f"{index + 1}. {item.title()}")

        case "edit":
            
            with open("file/student_name.txt","r") as file:
                student_name = file.readlines()
        
            number = int (input ("Enter the number you need to edit : "))
            number = number - 1
            newName = input ("Enter the student name : ") + "\n"
            
            with open("file/student_name.txt","w") as file:
                student_name[number] = newName
                file.writelines(student_name)

        case "delete":
            number = int (input ("Enter the number you need to delete the name : "))
            number = number - 1
            
            with open("file/student_name.txt" , "r") as file:
                student_name = file.readlines()

            with open("file/student_name.txt","w") as file:
                student_name.pop(number)
                file.writelines(student_name)

        case "exit":
            break
        
        case default:
            print ("wrong entered please try again")


            