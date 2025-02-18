result = {}

password = input ("Enter the password : ")

if len(password) >= 8:
    result["length"] = True
else :
    result["length"] = False

digit = False

for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

upperCase = False

for i in password:
    if i.isupper():
        upperCase = True

result["upperCase"] = upperCase

if all(result.values()) == True:
    print ("Strong password")
else:
    print ("Weak password")