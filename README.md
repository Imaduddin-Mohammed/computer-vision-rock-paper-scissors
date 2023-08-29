# Computer-Vision-Rock-Paper-Scissors
  > Rock-Paper-Scissors is a game in which a player simultaneously shows one of the three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.


### To run this game yourself please follow the steps below
- First you have to clone this repository to your local machine. Create a directory where you want to save the game and then *paste this code* in the terminal:
``` git clone <https://github.com/Imaduddin-Mohammed/computer-vision-rock-paper-scissors.git> ```
- To install the dependencies from file named **requirements.txt**, make sure you do this in the intended environment you wish to install, *copy and paste* the following code:
```python
pip install requirements.txt
```
- Now activate the environment in which you have these dependencies installed, then in bash terminal run the following code:
```python
python camera_rps.py
```
- Now provide the input to the camera in the form of 'Rock' or 'Paper' or 'Scissors' or 'Nothing' and pressing **q** on the keyboard will feed the input, this will be looped until one of the player finally wins
- Once a player wins, the game is terminated and winner is printed to the console.

## Milestone 1 
> Setting up the environment
  > Created a git repository for this project and cloned it to my local machine.

## Milestone 2
> Creating the Computer Vision System
  > First task will involve creating the model which is basically the webcam of computer recognizing the inputs rock, paper, scissors and nothing as input.

### Task 1
> Creating image project model which has 4 classes namely ROCK, PAPER, SCISSORS, NOTHING
> Google's Teachable machine was used to train the 4 classes and train the model.
### Task 2 
> Downloading the trained model from Tensorflow tab of Teachable Machine in keras format and named the file **keras_model.h5** and its labels as **labels.txt**
> These files contain the structure and the parameters of the deep learning model.
### Task 3
>



