import cv2
import random
from keras.models import load_model
import numpy as np
import time


class RockPaperScissor:
    def __init__(self):
        self.number_of_rounds = 3
        self.computer_wins = 0
        self.user_wins = 0

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

    def load_model(self):
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

    def get_winner(self, computer_choice, user_choice):
        while self.computer_wins < 3 or self.user_wins < 3:
            if (computer_choice == 'Rock' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Scissors') or (computer_choice == 'Scissors' and user_choice == 'Rock'):
                self.user_wins +=1
                print("You Won!")
                return self.user_wins
            elif computer_choice == user_choice:
                print("It's a Tie!")
            else:
                self.computer_wins +=1
                print("You Lost!, Computer is the winner")
            return self.computer_wins 
    
    def play(self):
        while self.number_of_rounds < 3: 
            self.get_computer_choice()
            self.load_model()
            self. get_winner(self.computer_choice, self.user_choice)
            

game = RockPaperScissor()
game.play()