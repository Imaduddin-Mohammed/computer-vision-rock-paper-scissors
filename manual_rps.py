#Task 1
import random

inputs = ['Rock','Paper','Scissors']

def get_computer_choice():
    computer_choice = random.choice(inputs)
    return computer_choice

def get_user_choice():
    user_selected_input = input("please enter input : ")
    return user_selected_input

# Saving function outputs to variables
get_computer_choice = get_computer_choice()
get_user_choice = get_user_choice()

#Task 2 

def get_winner(get_computer_choice,get_user_choice):
    winner = ''
    if get_computer_choice or get_user_choice not in inputs:
        print("Invalid inputs")
    else:
        if (get_computer_choice == 'Rock' and get_user_choice == 'Paper') or (get_computer_choice == 'Paper' and get_user_choice == 'Scissors') or (get_computer_choice == 'Scissors' and get_user_choice == 'Rock'):
            winner = 'Computer'
            print("You lost")
        elif get_computer_choice == get_user_choice:
            print("It's a Tie!")
        else:
            winner = 'User'
            print("You won!")
    return winner 
