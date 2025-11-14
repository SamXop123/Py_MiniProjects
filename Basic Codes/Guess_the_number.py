
#Guess the Number game

import random

print("Guess the Number!")

random_num = random.randint(1, 100)

attempt = 0

while True:
    entered = input("Enter any Number(1 to 100) OR Quit(Q): ")


    if (entered == "Q") :
        print("You Coward! Quitting a game shows your cowardness not bravery!")
        break

    try:
        
        entered = int(entered)

        if (entered == random_num) :
            print(f"Congratulations! \nYou guessed the right number. The number was {random_num}")
            print("-----YOU WON-----")
            print("Total Attempts: ", attempt)
            break

        elif (entered < random_num) :
            print("Too Low!\nTry Again.")
            
        else:
            print("Too High! \nTry Again.")
            
        attempt += 1

    except ValueError:
        print("Invalid Input. Please enter a valid number.")



print()
