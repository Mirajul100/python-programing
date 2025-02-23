import FreeSimpleGUI as frame
import function

label = frame.Text("Enter the Employee Name : " , tooltip="Enter Employee")
inputBox = frame.InputText(tooltip="Enter the Employee Name" , key="employee")
addButton = frame.Button("Add")

windows = frame.Window("Employee management" ,
                        layout=[[label] , 
                        [inputBox , addButton]] , 
                        font=("Roboto",18))

while True:
    userInput , value = windows.read()
    print (userInput)
    print (value)

    match userInput:
        case "Add":
            employee = function.readFile()
            newEmployee = value["employee"]+"\n"
            employee.append(newEmployee)
            function.writeFile(employee)
        case frame.WIN_CLOSED:
            break

windows.close()