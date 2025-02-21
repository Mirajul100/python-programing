def readFile(filePath = "file/employ.txt"):
    with open (filePath , "r") as file:
        File = file.readlines()
    return File


def writeFile(employName,filePath  = "file/employ.txt"):
    with open (filePath , "w") as file:
        file.writelines(employName)
