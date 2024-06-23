import random

user_wins = 0
pc_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type: Rock/Paper/Scissor or Bye to quit: ").lower()
    if user_input == "Bye":
        break
        
    if user_input not in options:
        print("Please try again")
        continue

    user_num = random.randint(0, 2)
    # ROCK = 0 / PAPER = 1 / SCISSOR = 2
    computer_pick = options[user_num]
    print("The Computer choosed: " + computer_pick)

    if user_input == "Rock" and computer_pick == "Scissor":
        print("You won!!")
        user_input += 1
        

    elif user_input == "Paper" and computer_pick == "Rock":
        print("You won!!!")
        user_input += 1
        

    elif user_input == "Scissor" and computer_pick == "Paper":
        print("You won!!!")
        user_input += 1

    else:
        print("OOps you lost!")
        pc_wins += 1    

print("You won " + str(user_wins) + " times.")
print("The computer won " + str(pc_wins) + " times.")                    