
print("Please choose an operation to use: ")
print("1) ADD")
print("2) SUBTRACT")
print("3) MULITPLY")
print("4) DIVIDE")

options=input()

if options == "1":
    num1 = input("Please enter the first digit: ")
    num2 = input("Please enter the second digit: ")
    print("The sum of the numbers is " + str(int(num1) + int(num2)))
elif options == "2":
    num1 = input("Please enter the first digit: ")
    num2 = input("Please enter the second digit: ")
    print("the answer of the question is " + str(int(num1) - int(num2)))
elif options == "3":
    num1 = input("Please enter the first digit: ")
    num2 = input("Please enter the second digit: ")
    print("The product of the question is " + str(int(num1) * int(num2)))
elif options == "4":
    num1 = input("Please enter the first digit: ")
    num2 = input("Please enter the second digit: ")
    print("The answer of this question is " + str(int(num1) / int(num2)))
else:
    print("Invalid entered data, please try again")
    quit()