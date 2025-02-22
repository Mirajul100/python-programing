import json

with open ("qAnswer.json" , "r") as file:
    contain = file.read()

data = json.loads(contain)

for item in data:
    print (item["question"])
    for index , userChoice in enumerate(item["choice"]):
        print (f"{index + 1}-{userChoice}")
    userInput = int (input("Enter the Answer : "))
    item["userInput"] = userInput

score = 0
    
for item in data:
    if item["userInput"] == item["correct_Answer"]:
        print ("Correct")
        score += 1
    else:
        print ("Wrong")

    print (f"Your answer is {item["userInput"]} The correct answer is {item['correct_Answer']}")

print (f"{score} / {len(data)}")