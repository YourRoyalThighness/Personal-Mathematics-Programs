import re
def opIdent():
    opInput = str(input("Equation: "))
    opList = ["+", "-", "*", "/", "**"]
    for i in range(len(opList)):
        if opInput == opList[i]:
            print("success")
            break
        else:
            print("failure")
opIdent()
