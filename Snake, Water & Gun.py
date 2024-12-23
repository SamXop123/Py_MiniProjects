import random

def snake_water_gun():
    print("\n---- SNAKE WATER GUN ----\n")

    # Options
    choices = ["snake", "water", "gun"]

    # Generate Random choice
    computer_choice = random.choice(choices)

    # Get user's choice
    user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()

    if user_choice not in choices:
        print("Invalid choice! Please select either Snake, Water, or Gun.")
        return

    # Display choices
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine the result
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        print("You won!")
    else:
        print("Computer wins!")

snake_water_gun()

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


