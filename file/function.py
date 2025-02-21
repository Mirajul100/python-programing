FILEPATH = "file/employ.txt"

def readFile(filePath = FILEPATH):
    with open (filePath , "r") as file:
        File = file.readlines()
    return File


def writeFile(employName,filePath  = FILEPATH):
    with open (filePath , "w") as file:
        file.writelines(employName)
