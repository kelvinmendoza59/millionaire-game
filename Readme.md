Who Wants to Be a Millionaire? - Terminal Game
A Python-based implementation of the classic quiz show "Who Wants to Be a Millionaire?" that runs in your terminal.
Features

Multiple-choice questions with increasing difficulty
Progressive prize money system
Option to quit with current winnings
Player name customization
Dramatic reveals and pauses for tension
Clear screen functionality for better readability
Play again feature

Requirements

Python 3.6 or higher
No external dependencies required

Installation

Clone this repository:

bashCopygit clone https://github.com/your-username/millionaire-game.git
cd millionaire-game

Run the game:

bashCopypython millionaire_game.py
How to Play

Enter your name when prompted
Read each question carefully
Choose your answer by typing A, B, C, or D
Press Q at any time to quit with your current winnings
Try to reach the £1,000,000 prize!

Code Structure

GameConfig: Contains game configuration settings
Player: Manages player data and progress
Question: Represents individual quiz questions
GameDisplay: Handles all display-related functionality
QuestionBank: Manages the question database
GameManager: Controls game flow and logic

Development
The code follows object-oriented principles and is structured for easy maintenance and extension. Key improvements in the latest version include:

Better code organization with separate classes for different responsibilities
Type hints for better code clarity
Improved error handling
More consistent code style
Better separation of concerns

Future Improvements

Add more questions to the question bank
Implement lifelines (50:50, Phone a Friend, Ask the Audience)
Add sound effects
Save high scores
Add difficulty levels

Contributing

Feel free to fork this repository and submit pull requests with improvements!

License

This project is licensed under the MIT License - see the LICENSE file for details.