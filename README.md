# PY2048

#### Video Demo:  <https://youtu.be/kb9NuWyixiY>

## Summary

PYS2048 is a python implementation of the classic game 2048 using the pygame library. However, unlike the original version, this implementation includes a timer that adds a random 2 or 4 tile to the board when it hits 0. This timer is reset upon the player making a move, and can be adjusted using a button in the game called "Speed." This allows for new strategies for beating the game and adds a pressure to do each move quickly and precisely. 


## Files

**main.py:** This file contains a basic game loop structure that utilizes the pygame library. The code manages the transitions between the different screens (title, game and instructions). This is done through an infinite loop that checks for return statements on the other files that say which game state should come next. This is the file that is run to launch the game, which defaults to the title screen. The main loop in the file also handles for when the user closes the game.

**title.py:** This controls the first screen that appears. This screen includes a play button, which returns the "game", causing the screen to change to the main game screen. It also includes a button that leads to the instructions, which would cause the file to return "instructions."  These buttons help make it clear for players how to navigate around the game and is a clean setup for the initial window. The file also has code to detect when the user closes the game.

**instructions.py:** This file controls the instructions screen with the keybinds and the goal of the game. Below the instructions, there is a return button that sends the user back to the title screen. This is done by setting the "running" variable to false, which the main file then uses as a signal to go to the title screen.

**game.py:** This file is the bulk of the game's code. After initalizing the dimensions of the window, there are several functions that control different aspects of the game. The game works by aligning all non zero numbers in the direction specified and then doubling/removing numbers if two of the same number are next to each other. This is only possible because 2048 works by moving all numbers to the furthest point in one direction on each move. 
- reset_game(): resets the game board, score, and move timer to their original states. It clears the board by setting all the values in a 2D array to 0 and places two starting tiles using the spawnRandTile function twice. The parameter "force_two=True" is used in order to ensure that only twos are spawned in the beginning, and not 4s. Below are some important functions used:
- spawnRandTile(force_two=False): This function randomly selects a cell on the board that has a value of 0 and replaces it with a value of 2 or 4. The "force_two" paramter is set to false as default to ensure that both 2 and 4 tiles are created while the game is played
- shift(row): This function is a helper function that prepares rows for merging and makes sure tiles are aligned. This is used in the move functions
- game(): Main function that handles user input and game state

## Game Choices

Most other 2048 implementions include sliding and merging animations when playing, but mine does not include this due to the high difficulty of implementation and the desire for the game to feel as fast as possible. When there is a lack of animation, the game state changes immediately, forcing the player to adapt and make their next move quickly. This idea of speed came from my interest in speedrunning, which is completing an objective in a video as fast as possible. To further this effect, the timer was added to create pressure and make the game feel more intense (as the classic version allows for a lot of time to think). 

I split my files by game scene for organization and to reduce interdependecy errors that I ran into while making the project. This allowed me debug functions that only impacted one scene without altering or introducing bugs into other functions. 

