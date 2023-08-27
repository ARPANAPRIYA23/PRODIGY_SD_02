#Create a guessing game

import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < target_number:
                print("Your guess is too low. Try again.")
            elif user_guess > target_number:
                print("Your guess is too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
