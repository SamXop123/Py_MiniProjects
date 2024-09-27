
print()
print("----SNAKE WATER GUN----") 
print()

import random

game = ["Snake", "Water", "Gun"]

auto_choice = random.choice(game)
print(auto_choice)
user_choice = input("Enter your choice: ")

user_choice = user_choice.lower()
auto_choice = auto_choice.lower()

if (user_choice == auto_choice):
    print("Draw!")

elif (user_choice == "snake" and auto_choice == "water") or \
     (user_choice == "water" and auto_choice == "gun") or \
     (user_choice == "gun" and auto_choice == "snake"):
    print("You won!")

else:
    print("Computer Wins")

print("#----------------------------------------")

#ANOTHER METHOD :

def swg(swg):
    game = ["Snake", "Water", "Gun"]
    auto_choice = random.choice(game)

    print(f"Computer choice: {auto_choice}")
    print(f"Your choice: {swg}")

    swg = swg.lower()
    auto_choice = auto_choice.lower()

    if (swg == auto_choice):
        print("Draw!")

    elif (swg == "snake" and auto_choice == "water") or \
         (swg == "water" and auto_choice == "gun") or \
         (swg == "gun" and auto_choice == "snake"):
        print("You won!")
    else:
        print("Computer won!")

your_choice = input("Enter your choice: ")
print()
swg(your_choice)


