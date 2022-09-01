userInput = input("Sano luku: ")
maxValue = minValue = int(input("Sano luku: "))

while userInput != "":
    userInput = input("Sano luku: ")
    if userInput == "":
        break
    userInputInt = int(userInput)
    if userInputInt < minValue:
        minValue = userInputInt
    if userInputInt > maxValue:
        maxValue = userInputInt
    userInput = input("Sano luku: ")
print(f"Pienin arvo: {minValue}, suurin arvo: {maxValue}")
