The "Guess-A-Number" Game

<img width="478" height="399" alt="image" src="https://github.com/user-attachments/assets/0df83d2f-4d52-4bcc-8dbf-e00e439e854c" />

A console-based Python implementation of the classic number guessing game with progressive difficulty levels.

  Project Goals

This project implements an interactive number guessing game that challenges players to guess a randomly generated number within a limited number of attempts. The game features:

Progressive Difficulty: 10 levels with increasing number ranges (Level 1: 1-100, Level 2: 1-200, ..., Level 10: 1-1000)
Educational Purpose: Helps players develop logical thinking and number estimation skills
Entertainment: Provides an engaging gaming experience with level progression
Input Validation: Ensures robust user experience with proper error handling

  Solution

  Algorithm
The game uses a binary search-like approach where:
1. Computer generates a random number within the current level's range
2. Player inputs their guess
3. System provides feedback ("Too High", "Too Low", or "Correct")
4. Player has up to 10 attempts per level
5. Upon success, player advances to the next level with a larger range

  Technologies Used
Python 3.x: Core programming language
random module: For generating random numbers
Built-in input/output functions: For user interaction
Control structures: while loops, if-else statements for game logic

  Key Features
Level System: 10 progressive difficulty levels
Input Validation: Handles invalid inputs gracefully
Range Validation: Ensures guesses are within valid range
Game State Management: Tracks current level and attempts
Restart Functionality: Option to restart from level 1 after game over
Victory Condition: Complete celebration upon finishing all levels

  Source Code

You can find the complete source code in the main Python file:
[Source Code](guess_a_number.py)

  Screenshots

  Game Start
  
<img width="408" height="55" alt="image" src="https://github.com/user-attachments/assets/53e572a4-aa58-4016-bb53-4d574668ad0c" />

  Gameplay

<img width="318" height="383" alt="image" src="https://github.com/user-attachments/assets/c080172b-9b24-43e0-a6d1-ec25923a9444" />

  Level Progression

<img width="294" height="71" alt="image" src="https://github.com/user-attachments/assets/02cab486-5acc-4d40-9746-561e0b9494d2" />

  Game Over

<img width="331" height="160" alt="image" src="https://github.com/user-attachments/assets/d645505d-9d44-45a0-b4c2-f0957f0c0c84" />


  Live Demo

To run the game locally:

1. Prerequisites: Ensure you have Python 3.x installed
2. Download: Clone or download the source code
3. Run: Execute the following command in your terminal:
   bash
   python guess_a_number.py
4. Play: Follow the on-screen instructions to play!

  Online Demo
  
[<img alt="Play Game" src="https://github.com/user-attachments/assets/05919707-5ba1-4270-8dcc-0af505ab4527" />](https://replit.com/@vaskozaikov/GuessANumberByVasko#guess_a_number.py)

  Game Rules

1. Objective: Guess the computer's number within 10 attempts
2. Levels: Complete 10 levels with increasing difficulty
3. Ranges: 
   - Level 1: 1-100
   - Level 2: 1-200
   - ...
   - Level 10: 1-1000
4. Feedback: Receive "Too High", "Too Low", or success messages
5. Victory: Complete all 10 levels to win the entire game!

---

Enjoy the game and challenge yourself to reach Level 10!
