import FreeSimpleGUI as frame
import function

label = frame.Text("Enter the Employee Name : " , tooltip="Enter Employee")

inputBox = frame.InputText(tooltip="Enter the Employee Name" , key="employee")

addButton = frame.Button("Add")

ListBox = frame.Listbox(values=function.readFile() ,
                      key="edit" , 
                      enable_events= True ,
                      size=(50 , 10))

editButton = frame.Button("Edit")

deleteButton = frame.Button("Delete")

exitButton = frame.Button("Exit")

windows = frame.Window("Employee management",
                        layout=[[label] , 
                        [inputBox , addButton], 
                        [ListBox ,editButton , deleteButton],
                        [exitButton]] , 
                        font=("Helvetica",18))

while True:
    userInput , value = windows.read()
    print (userInput)
    print (value)

    match userInput:
        case "Add":
            employee = function.readFile()
            newEmployee = value['employee']+"\n"
            employee.append(newEmployee)
            function.writeFile(employee)
            windows['edit'].update(values=employee)
            windows["employee"].update(value="")

        case "Edit":
            select = value['edit'][0]
            newEdit = value['employee']

            employees = function.readFile()
            index = employees.index(select)
            employees[index] = newEdit
            function.writeFile(employees)
            windows['edit'].update(values=employees)
            windows["employee"].update(value="")

        case "edit":
            windows['employee'].update(value= value['edit'][0])

        case "Delete":
            emp = value["edit"][0]
            employee = function.readFile()
            employee.remove(emp)
            function.writeFile(employee)
            windows["edit"].update(values=employee)
            windows["employee"].update(value="")

        case "Exit":
            break

        case frame.WIN_CLOSED:
            break

windows.close()