import random

levels = {
    1: 100,
    2: 200,
    3: 300,
    4: 400,
    5: 500,
    6: 600,
    7: 700,
    8: 800,
    9: 900,
    10: 1000
}

current_level = 1

print("Welcome to the Level-based Number Guessing Game!")
print("Complete all 10 levels to win the entire game!")

while True:

    if current_level > 10:
        print("\nCONGRATULATIONS! You completed all 10 levels!")
        print("You are a true number guessing master!")
        break

    max_number = levels[current_level]
    print(f"\n--- LEVEL {current_level} ---")
    print(f"Guess a number between 1 and {max_number}")

    computer_number = random.randint(1, max_number)
    tries = 0

    while tries < 10:
        player_input = input(f"Guess the number (1-{max_number}): ")

        if not player_input.isdigit():
            print("Invalid input! Try again: ")
            continue

        player_number = int(player_input)

        if player_number < 1 or player_number > max_number:
            print(f"Please enter a number between 1 and {max_number}!")
            continue

        if player_number == computer_number:
            print(f"You guessed it! The number was {computer_number}")
            print(f"Level {current_level} completed!")
            current_level += 1
            break

        elif player_number > computer_number:
            print("Too High!")

        else:
            print("Too Low!")

        tries += 1

    if tries == 10:

        print(f"Game over! The number was {computer_number}")
        print(f"You reached level {current_level}")

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                print("\nRestarting from level 1...")
                current_level = 1
                break
            elif play_again == "no":
                print("Thanks for playing! Goodbye!")
                exit()
            else:
                print("Please enter 'yes' or 'no'.")
