while True :
    user_input = input ("Enter add , show , edit , delete , exit : ")
    user_input = user_input.strip()

    match user_input.lower():
        case "add":
            studentName = input ("Enter the student name : ") + "\n"
            file = open('file/student_name.txt' , "r")
            student_name = file.readlines()
            file.close()

            student_name.append(studentName)

            file = open('file/student_name.txt' , "w")
            file.writelines(student_name)
            file.close()

        case "show":
            file = open("file/student_name.txt" , "r")
            student_name = file.readlines()
            file.close()

            for index , item in enumerate(student_name) :
                print (f"{index + 1}. {item.title()}")

        case "edit":
            number = int (input ("Enter the number you need to edit : "))
            number = number - 1
            newName = input ("Enter the student name : ")
            student_name[number] = newName

        case "delete":
            number = int (input ("Enter the number you need to delete the name : "))
            number = number + 1
            student_name = student_name.pop(number)

        case "exit":
            break
        
        case default:
            print ("wrong entered please try again")


            