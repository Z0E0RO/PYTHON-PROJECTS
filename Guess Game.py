import random

x = int(input("The range of the guess:\t"))
secret_number = random.randint(0,x)
guess_count = 0
guessed_number = 0
total_guesses = 2

while guess_count < 3:
    guessed_number = int(input(f"Guess the number between 0 and {x} :\t"))
    if guessed_number == secret_number:
        print(f"You Won! You have guessed the correct number which is {secret_number}")
        break
    elif guessed_number > secret_number and total_guesses != 0:
        print("The number you guessed is larger. Try Again!")
    elif guessed_number < secret_number and total_guesses != 0:
        print("The number you guessed is smaller. Try Again!")
    print(f"Number of guesses left {total_guesses}")
    if total_guesses == 0:
        print("You lost! You are out of guesses.")
    total_guesses -= 1
    guess_count += 1

