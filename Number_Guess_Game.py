import random

def guessing_game():
    print()
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break

guessing_game()
