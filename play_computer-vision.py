import manual_rps

def play():
    
    manual_rps.get_computer_choice()
    manual_rps.get_user_choice()
    manual_rps.get_winner(manual_rps.computer_choice,manual_rps.user_choice)

play()
    