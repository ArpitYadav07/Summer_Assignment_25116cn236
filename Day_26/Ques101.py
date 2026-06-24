# Number Guessing Game
from random import randint

number = randint(1, 100)

while True:
    guess = int(input("Enter guess: "))

    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too Low")
    else:
        print("Too High")