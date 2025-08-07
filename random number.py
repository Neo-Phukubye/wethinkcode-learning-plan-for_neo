import random

guess= int(input("Guess the secret number from 1 to 10: "))

random_number = random.randint(1, 10)

if guess == random_number:
    print("Congratulations, You have guessed the secret number!")
elif guess > random_number:
    print("Too high!")
else:
    print("Too low!")