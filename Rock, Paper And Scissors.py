import random


choices = ['p','s','r']
def play():
    user = input("Type 'p' for paper, 's' for scissors and 'r' for rock\n")
    computer = random.choice(choices)
    if user == computer:
        return "It's a draw"

    if win(user,computer):
        return "Youn Won!"

    return "You Lost!"

   
def win(you,opponent):
    if (you == 'p' and opponent == 's') or (you == 'r' and opponent == 's') or (you == 's' and opponent == 'p'):
        return True

print(play())
