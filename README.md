# Computer-Vision-Rock-Paper-Scissors
  > Rock-Paper-Scissors is a game in which a player simultaneously shows one of the three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.


### To run this game yourself please follow the steps below
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
- Google's Teachable machine was used to train the 4 classes and train the model.
![Google's Teachable Machine]()
### Task 2 
- Downloading the trained model from Tensorflow tab of Teachable Machine in keras format and named the file **keras_model.h5** and its labels as **labels.txt**
- These files contain the structure and the parameters of the deep learning model.

## Milestone 3
> Installing the Dependencies and Ensuring the Computer Vision System Works
### Task1
- Created a new Virtual Environment
- The following dependencies are essential for this project, installed them using *``` pip install <packagename> ```*
   > opencv-python,tensorflow, ipykernel
### Task2
> To ensure that the *keras_model.h5* model works I ran the following code:
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
- The main thing in the above code is the **prediction** variable which will containg the output in the form of floating numbers which are rock, paper, scissors and nothing probabilities respectively.
- For example, if the prediction has the following output: ==[[0.8, 0.1, 0.05, 0.05]]==, there is an 80% chance that the input image shows rock, a 10% chance that it shows paper, a 5% chance that it shows scissors, and a 5% chance that it shows nothing
Predictions holds a list of probabilites as shown below
![Prediction variable]()

# Milestone 4
> Created a python script that will simulate the rock paper scissors game and compare the input with the computer's choice and show the winner
##Task 1
- Storing the users and computer's choice in variables 
- This is done manually without a camera as shown below 
![manual_rps.py]()






