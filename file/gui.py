import FreeSimpleGUI as frame

label = frame.Text("Enter the Employee Name : ")
inputBox = frame.InputText(tooltip="Enter the Employee Name")
addButton = frame.Button("Add")

windows = frame.Window("Employee management" , layout=[[label] , [inputBox , addButton]])
windows.read()
windows.close()