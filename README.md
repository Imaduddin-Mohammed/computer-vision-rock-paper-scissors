# Computer-Vision-Rock-Paper-Scissors
  > Rock-Paper-Scissors is a game in which a player simultaneously shows one of the three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Please follow the instructions below to play the game.
- First you have to clone this repository to your local machine. Create a directory where you want to save the game and then *paste this code* in the terminal:
``` git clone <https://github.com/Imaduddin-Mohammed/computer-vision-rock-paper-scissors.git> ```
- Next install the dependencies from file named **requirements.txt**, make sure you do this in the intended environment you wish to install, then *copy and paste* the following code:
```python
pip install requirements.txt
```
- Now activate the environment in which you have these dependencies installed, then in bash terminal run the following code:
```python
python camera_rps.py
```
- Now provide the input to the camera in the form of 'Rock' or 'Paper' or 'Scissors' or 'Nothing' and pressing **q** on the keyboard will feed the input, this will be looped until one of the player wins the game.
- Finally the Winner is printed to the console and the game ends!

## Milestone 1 
> Setting up the environment
  - Created a git repository for this project and cloned it to my local machine.

## Milestone 2
> Creating the Computer Vision System.

### Task 1
- Creating image project model which has 4 classes namely Rock, Paper, Scissors and Nothing
- Google's Teachable machine was used to train the 4 classes and train the model as shown below
![training_model](computer-vision-rock-paper-scissors\teachable_machine_model_training.png)
### Task 2 
- Downloading the trained model from Tensorflow tab of Teachable Machine in keras format and named the file **keras_model.h5** and its labels as **labels.txt**
- These files contain the structure and the parameters of the deep learning model.

## Milestone 3
> Installing the Dependencies and Ensuring the Computer Vision System Works
### Task1
- Created a new Virtual Environment
- The following dependencies are essential for this project, installed them using *``` pip install <packagename> ```*
   > opencv-python, tensorflow, ipykernel
### Task2
> To ensure that the **keras_model.h5** model works I ran the following code:
```python
import cv2
from keras.models import load_model
import numpy as np
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
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
- The main thing in the above code is the *prediction* variable which will containg the output in the form of floating numbers which are rock, paper, scissors and nothing probabilities respectively.
- For example, if the prediction has the following output: [[0.8, 0.1, 0.05, 0.05]], there is an 80% chance that the input image shows rock, a 10% chance that it shows paper, a 5% chance that it shows scissors, and a 5% chance that it shows nothing
- Predictions holds a list of probabilites as shown below
![Prediction]()

## Milestone 4
> Creating a python script that will simulate the rock paper scissors game and compare the input with the computer's choice and show the winner
### Task 1
- Storing the users and computer's choice in variables 
- This is done manually without a camera as shown below 
![manual_game](computer-vision-rock-paper-scissors\manual_rps.png)
### Task 2
> Finding out who won
- Introduced if-elif-else statements, the script should now choose a winner based on the classic rules of Rock-Paper-Scissors
- For example, if the computer chooses rock and the user chooses scissors, the computer wins
- Defined a function called get_winner which will return the *winner* as shown in the image in Task1
### Task 3 
> Creating a function that will play the game
- All the code in **manual_rps.py** is now part of the game, hence wrapping it up in a function called *play* in **play_computer-vision.py**
![Play_game]()

## Milestone 5
> Using the Camera to play the game
### Task1 
> Putting it all together
- Replacing the hard-coded user guess in **manual_rps.py** by the trained model **keras_model.h5** so that the camera will guess
- Creating a new file **camera_rps.py** 
  - Created a class called **RockPaperScissor*
  - defined 2 Attributes *computer_wins* & *user_wins* and initilized them to 0
  - *get_computer_choice()* returns the computer choice randomly
  - *get_user_choice()* returns the user choice, wherein  I have used the *.argmax()* method of the numpy library to select the index of the highest probability from *predictions* list.
### Task 2
> Adding countdown timer for each round
- Added a timer of 3 seconds before each input can be given

```python
start_time = time.time()
            while time.time() - start_time <=3:
                print(3 - int(time.time() - start_time))
```                
- The above code will print *1, 2 & 3* on the console and then the camera opens to capture the input, this ensures that the user has enough time to prepare for the next round.
### Task 3
> Repeating until a player gets 3 victories
- In the *get_winner()* introduced a while loop that ensures this.
```python
def get_winner(self):
  while self.computer_wins and self.user_wins <3:
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
```





















