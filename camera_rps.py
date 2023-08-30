"""
This file contains all the code that will start the camera and capture the user choice and compare it with the random computer choice and prints the winner of the game.

All the logic defined earlier in manual_rps.py and play_computer-vision.py is present in this file. Additionally it contains the function "load_model()" which is
essential to load the trained keras_model.h5"
Once the camera starts the user provides the input in the form of hand gesture showing either(Rock/Paper/Scissors/Nothing)
"""


import cv2
import random
from keras.models import load_model
import numpy as np
import time


class RockPaperScissor:
    """ 
    This class contains methods that are essential to play the computer vision RockPaperScissors game.

    It contains the following five(5) methods:
    get_computer_choice()
    get_user_choice()
    load_model()
    get_winner()
    play()

    Attributes:
        number_of_rounds(int): This variable is initialized to integer 3 which means there will be 3 rounds for each player to give their input.
        computer_wins(int): This variable keeps track of the computer score.
        user_wins(int): This variable keeps track of the user score.
    """
    def __init__(self):
        """Constructor for the class"""
        self.computer_wins = 0
        self.user_wins = 0

    def get_computer_choice(self):
        """"
        This function captures the computer choice randomly & the choice() method of random module is used to capture a value from the list of values: [Rock, Paper, Scissors]

        Returns:
            computer_choice(variable):Contains any 1 value from this list [Rock, Paper, Scissors].
        """
        self.computer_choice = random.choice(['Rock','Paper','Scissors'])
        return self.computer_choice
        
    def get_user_choice(self,prediction):
        """
        This function will calculate the user_choice

        Args:
            prediction(list):A list which contains the probabilities of 4 classes Rock, Paper, Scissors and Nothing

        Returns:
            user_choice(variable): This is a variable which will contain the the user input shown to the camera.

        This function takes in prediction as an argument and has 3 if statements to select user_choice as Rock or Paper or Scissors based on the prediction(list) else it will choose Nothing class
        To select the index which has the highest value from prediciton, argmax() method of numpy library is used.
        user_choice is retuned in each if-else statement, which will contain the index of highest probablity from the list
        """
        if np.argmax(prediction) == 0:
            self.user_choice = 'Rock'
            return self.user_choice
        elif np.argmax(prediction) == 1:
            self.user_choice = 'Paper'
            return self.user_choice
        elif np.argmax(prediction) == 2:
            self.user_choice = 'Scissors'
            return self.user_choice 
        else:
            self.user_choice = 'Nothing'
            return self.user_choice

    def load_model(self):
            """
            This function contains the code to load the trained model "keras_model.h5"

            The function contains all the code to open the camera and capture the input of the user
            If "q" is pressed on the keyboard this will capture the image i.e user_choice and close the camera and exit the while loop
            Inside the while loop, get_user_choice(prediction) function is called by passing the prediction as argument which returns user_choice.

            Returns:
                prediction(list): A list which contains probabilites of 4 classes, Rock, Paper, Scissors & Nothing class
            """
            # elapsed time is calculated since the camera starts recording the input until the user presses "q"
            start_time = time.time()
            model = load_model('keras_model.h5')
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            countdown = start_time + 5
            while True: 
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow('frame', frame)
                self.get_user_choice(prediction)
                print(countdown - start_time)
                # Press q to close the window
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break 
            current_time = time.time()
            elapsed_time = {current_time - start_time}
            print(f"Time elapsed: {elapsed_time} seconds since the script started")
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

    def get_winner(self):
        """
        This function returns the winner

        A while loop is created based on the condition that if any one of the attributes: user_wins or computer_wins is less than 3 the loop keeps on running.
        To select the winner if-else statements are constructed based on the logic of Rock, Paper, Scissors game
        One winner is returned

        Returns:
            user_wins(int):This is the score of user
            computer_wins(int):This is the score of computer
        """
        while self.computer_wins < 3 or self.user_wins < 3:
            if (self.computer_choice == 'Rock' and self.user_choice == 'Paper') or (self.computer_choice == 'Paper' and self.user_choice == 'Scissors') or (self.computer_choice == 'Scissors' and self.user_choice == 'Rock'):
                self.user_wins +=1
                print("You Won!")
                return self.user_wins
            elif self.computer_choice == self.user_choice:
                print("It's a Tie!")
            else:
                self.computer_wins +=1
                print("You Lost!, Computer is the winner")
            return self.computer_wins 
    
    def play(self):
        """This function will start the game"""
        while True:
            self.get_computer_choice()
            self.load_model()
            self.get_winner()
            print(f"No. of runs: user chose : {self.user_choice}, computer chose : {self.computer_choice}")
            print(f"user score is : {self.user_wins} computer score is : {self.computer_wins}")
            if self.user_wins == 3:
                print("User wins")
                exit()
            elif self.computer_wins ==3:
                print("Computer wins")
                exit()
game = RockPaperScissor()
game.play()






