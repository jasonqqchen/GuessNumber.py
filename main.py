import random
right_number = random.randrange(1,100)
input("Welcome to the Number Guess Game!")
User_selection = input("I'm thinking of a number between 1 and 100\n please choose a difficulty. Type 'easy' or 'hard ")

if User_selection == 'hard':
    print("you have 5 attempts to guess the number ")
    remaining_trial = 5 
else:
    remaining_trial = 10
    print("you have 10 attempts to guess the number")

is_game_over = False

while not is_game_over:
    user_guess = int(input("please guess the number "))
    if user_guess > right_number:
        remaining_trial -= 1
        print(f"Too high, you lose the one trial, remaining trial is {remaining_trial}")
        if remaining_trial == 0:
            is_game_over = True

    elif user_guess < right_number:
        remaining_trial -= 1
        print(f"Too low, you lose the one trial, remaining trial is {remaining_trial}")
        if remaining_trial == 0:
            is_game_over = True
    else:
        print(f"you got is the right number is {right_number}")
        is_game_over = True   
