name = input("Please type in your name: ")

answer = input("You have reached a crossroad, two options are layed infront of you, what would you choose? LEFT or RIGHT?: ").lower()

if answer == "left":
    q2 = input("You have reached a river, either you can cross the river through a bridge or walk along it to a forest, please type BRIDGE to cross the river or FOREST to walk alongside the river: ").lower()

    if q2 == "bridge":
        q4 = input("You crossed the bridge, reaching the other side of the bank, from there you took off to a wonderfull land filled with magical pleasure ")
    
    elif q2 == "walk":
         print("You walked across the river going to a forest filled with darkness and moist, you got cut by a poisonous plant")

    else:
        print("Invalid option, please try again, YOU LOSE")
        quit() 

elif answer == "Right":
    q3 = input("You have taken a RIGHT, now you have reached a house, would you like to sneak in and explore, or walk past the home? Type SNEAK to explore the home or WALK to walk past the house: ").lower()

    if q3 == "SNEAK":
        print("YOU DIED, there was a grandpa with a shotgun inside, the moment he saw you entering BLAM your brain was smeared into the back wall, you died for tresspassing the property")

    elif q3 == "WALK":
        q4 = input("You walked past the house, admiring its architect, you walked past the house and came to your car, sat in it and drove off")
    
    else:
        print("YOU LOSE, sorry invalid data entered")
        quit()

else:
    print("Invalid Option, please try again, YOU LOSE!")