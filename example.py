import cv2
import random
from keras.models import load_model
import numpy as np
import time


class Rockpaperscissor:
    def __init__(self):
        self.number_of_rounds = 3
        self.computer_score = 0
        self.user_score = 0
        self.user_choice = ''
        self.ccomputer_choice = ''

    def get_computer_choice(self):
        computer_choice = random.choice(['Rock','Paper','Scissors'])
        return computer_choice
    
    def get_user_choice(self,prediction):
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
        
    def get_winner(self,computer_choice,user_choice):
            if (self.computer_choice == 'Rock' and self.user_choice == 'Paper') or (self.computer_choice == 'Paper' and self.user_choice == 'Scissors') or (self.computer_choice == 'Scissors' and self.user_choice == 'Rock'):
                print("You Won!")
            elif self.computer_choice == self.user_choice:
                print("It's a Tie!")
            else:
                print("You Lost!, Computer is the winner")

    def load_model(self):
        while self.computer_score or self.user_score <3:
            start_time = time.time()
            print(start_time)
            model = load_model('keras_model.h5')
            cap = cv2.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            while True: 
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow('frame', frame)
                self.get_user_choice(prediction)
                # Press q to close the window
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break 
            current_time = time.time()
            print(current_time)
            elapsed_time = {current_time - start_time}
            print(f"Time elapsed: {elapsed_time} seconds since the script started")
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

 







