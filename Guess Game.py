import random

x = 10
secret_number = random.randint(0,x)
guessed_number = 0

while guessed_number != secret_number:
    guessed_number = int(input(f"Guess the number between 0 and {x} :\t"))
    if guessed_number > secret_number:
        print("The number you guessed is larger. Try Again!")
    elif guessed_number < secret_number:
        print("The number you guessed is smaller. Try Again!")


print(f"You Won! You have guessed the correct number which is {secret_number}")
