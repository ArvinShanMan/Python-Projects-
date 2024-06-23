import random

top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type in a digit")
    quit()

num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses = guesses + 1   
    user_guess = input("Please take a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type in a digit")
        continue
    
    if user_guess == num:
        print("Yess you got it")
        break
    elif user_guess > num:
            print("You were above the number")
    else:
        print("You were below the number")

print("Your Total guesses are " + str(guesses))