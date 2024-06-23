import random


calc = ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE"]
while True:
    calc = input("Please choose an operator ADD SUBTRACT MULTIPLY DIVIDE or type Q to quit ").lower()
    if calc == "Q":
        break

    if calc in ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE"]:
        continue

    calc = input()
    
    if calc == "ADD":
        num1 = input("Please enter the first digit: ")
        num2 = input("Please enter the second digit: ")
        print("The sum of this question is: " + str(int(num1) + int(num2)))
    
    elif calc == "SUBTRACT":
        num1 = input("Please enter the first digit: ")
        num2 = input("Please enter the second digit: ")
        print("The answer of this question is: " + str(int(num1) - int(num2)))
    
    elif calc == "MULTIPLY":
        num1 = input("Please enter the first digit: ")
        num2 = input("Please enter the second digit: ")
        print("The final product of the question is: " + str(int(num1) * int(num2)))
    
    elif calc == "DIVIDE":
        num1 = input("Please enter the first digit: ")
        num2 = input("Please enter the second digit: ")
        print("The final answer of this question is: " + str(int(num1) / int(num2)))

    else:
        print("Sorry invalid charecter please try again")
        continue



