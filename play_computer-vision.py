"""
This file runs the manual game

This file is an extension to the previous file manual_rps.py file which will start the game & ask for user input and prints out the winner to the console
"""
import manual_rps

def play():
    
    manual_rps.get_computer_choice()
    manual_rps.get_user_choice()    
    manual_rps.get_winner(manual_rps.computer_choice,manual_rps.user_choice)

play()
    
