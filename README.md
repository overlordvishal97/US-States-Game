# US-States-Game
This code creates a game that tests the user's knowledge of the 50 US states. The game uses the turtle library to display a map of the United States and the pandas library to read and manipulate data from a CSV file.

# Game Logic
The game starts by reading a CSV file containing the names and coordinates of all 50 US states. The game then enters a while loop that continues until the user has correctly identified all 50 states.

In each iteration of the loop, the game prompts the user to enter the name of a state. If the user enters "Exit", the game ends and a new CSV file is created containing the states that the user did not correctly identify.

If the user enters a correct state name, the game adds the state to the list of correct choices and uses the turtle library to write the state name on the map at the correct coordinates.

# How to Play
To play the game, simply run the code and follow the prompts. Enter the name of a US state, and the game will let you know if it is correct or not. If you enter "Exit", the game will end and a new CSV file will be created containing the states that you did not correctly identify.

# Note
This code assumes that you have a CSV file named "50_states.csv" containing the names and coordinates of all 50 US states. You will need to create this file or modify the code to use a different file. Additionally, you will need to have the turtle and pandas libraries installed.
