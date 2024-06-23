print("Hello, welcome to my computer quizz")
playing = input("Do you like to play a game? ").lower()
if playing != "Yes":
    print("Ok bye")
    quit()
    score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "Central Processing Unit":
    print("Yaay its Correct :)")
    score += 1
else:
    print("Sorry wrong answer")

answer = input("What does RLE stand for? ").lower()
if answer == "Run Length Encoding":
    print("Yes it's correct :)")
    score += 1
else:
    print("Sorry incorrect answer")

answer = input("What does MAC address stand for? ").lower()
if answer == "media access control":
    score += 1
    print("Correct!!!")
else:
    print("Sorry wrong answer")

answer = input("What does HTML stand for? ").lower()
if answer == "Hypertext Markup Language":
    score += 1
    print("Yes thats right!")
else:
    print("Sorry wrong answer")

answer = input("How many keys are there in a standard keyboard? ")
if answer == "101":
    score += 1
    print("Yes that is right!")
else:
    print("sorry thats wrong")

print("You got " + str(score) + " Questions Correct")
print("You got " + str(score/4 * 100) + " Questions Correct")