File = "Web/student.txt"

def readFile(filepath = File):

    with open (filepath , "r") as file:
        studentName = file.readlines()
    return studentName

def writeFile(studentInfo ,filepath = File):
    with open (filepath , "w") as file:
        file.writelines(studentInfo)

for name in readFile():
        print (name.title().strip("\n"))
