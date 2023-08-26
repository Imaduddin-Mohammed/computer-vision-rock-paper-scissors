"""
This file contains the logic of RockPaperScissors game

Individial functions are created for saving the user and computer choice, get_winner() function takes in the user & computer choice as parameters and 
prints the winner based on the hard coded logic of the game.
"""
#Task 1
import random

inputs = ['Rock','Paper','Scissors']

def get_computer_choice():
    computer_choice = random.choice(inputs)
    return computer_choice

def get_user_choice():
    user_selected_input = input("please enter input : ")
    return user_selected_input

#Task 2 
def get_winner(computer_choice,user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Scissors') or (computer_choice == 'Scissors' and user_choice == 'Rock'):
        print("You Won!")
    elif computer_choice == user_choice:
        print("It's a Tie!")
    else:
        print("You Lost!, Computer is the winner")


get_computer_choice()
get_user_choice()

computer_choice = get_computer_choice()
user_choice = get_user_choice()

get_winner(computer_choice,user_choice)
