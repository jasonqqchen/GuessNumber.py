import random

input("Welcome to the Number Guess Game!")
input("I'm thinking of a number between 1 and 100\n please choose a difficulty.")
User_selection = input("Type 'easy' or 'hard')
if User_selection == 'hard':
    print("you have 5 attempts remaining to guess the number")
    remaining_trial = 5 
else:
    remaining_trial = 10
    print("you have 10 attempts remaining to guess the number")

print(random.int)