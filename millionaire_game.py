import random
import time
import os
from typing import List, Optional

class GameConfig:
    """Configuration settings for the game"""
    INITIAL_PRIZE = 0
    DRAMATIC_PAUSE = 2
    QUICK_PAUSE = 1

class Player:
    """Represents a player in the game"""
    def __init__(self, name: str):
        self.name = name
        self.current_winnings = GameConfig.INITIAL_PRIZE
        self.questions_answered = 0

    def update_winnings(self, amount: int) -> None:
        """Update player's winnings"""
        self.current_winnings = amount
        self.questions_answered += 1

    def reset_game(self) -> None:
        """Reset player's game progress"""
        self.current_winnings = GameConfig.INITIAL_PRIZE
        self.questions_answered = 0

class Question:
    """Represents a single question in the game"""
    def __init__(self, question: str, options: List[str], correct_answer: str, prize_money: int):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.prize_money = prize_money

    def is_correct_answer(self, answer: str) -> bool:
        """Check if the provided answer is correct"""
        return answer == self.correct_answer

class GameDisplay:
    """Handles all game display functionality"""
    @staticmethod
    def clear_screen() -> None:
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_welcome() -> None:
        """Display welcome message and rules"""
        print("\n" + "="*50)
        print("Welcome to Who Wants to Be a Millionaire!")
        print("="*50)
        print("\nRules:")
        print("1. Answer questions correctly to win money")
        print("2. Each question is worth more money")
        print("3. You can walk away with your current winnings at any time")
        print("4. If you answer incorrectly, you lose!")
        print("\nPress Enter to begin...")
        input()

    @staticmethod
    def display_question(question: Question, question_number: int) -> None:
        """Display a question and its options"""
        GameDisplay.clear_screen()
        print(f"\nQuestion {question_number} for ${question.prize_money:,}")
        print("="*50)
        print(f"\n{question.question}\n")
        for option in question.options:
            print(option)
        print("\nEnter your answer (A, B, C, or D) or 'Q' to quit: ")

    @staticmethod
    def dramatic_reveal() -> None:
        """Add dramatic pause and ellipsis"""
        print("\nFinal answer?")
        time.sleep(GameConfig.DRAMATIC_PAUSE)
        print("...")
        time.sleep(GameConfig.QUICK_PAUSE)

class QuestionBank:
    """Manages the game's question database"""
    @staticmethod
    def load_questions() -> List[Question]:
        """Load and return all game questions"""
        return [
            Question(
                "What is the capital of France?",
                ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
                "C",
                1000
            ),
            # ... [previous questions remain the same]
            Question(
                "What is the name of the nearest galaxy to the Milky Way?",
                ["A) Andromeda", "B) Triangulum", "C) Centaurus A", "D) Sombrero"],
                "A",
                1000000
            )
        ]

class GameManager:
    """Manages the game flow and logic"""
    def __init__(self):
        self.display = GameDisplay()
        self.questions = QuestionBank.load_questions()

    def get_player_answer(self) -> str:
        """Get and validate player's answer"""
        while True:
            answer = input().upper()
            if answer in ['A', 'B', 'C', 'D', 'Q']:
                return answer
            print("Invalid input! Please enter A, B, C, D, or Q.")

    def play_game(self, player: Player) -> None:
        """Main game loop"""
        self.display.display_welcome()
        question_number = 1

        for question in self.questions:
            self.display.display_question(question, question_number)
            player_answer = self.get_player_answer()

            if player_answer == 'Q':
                print(f"\nThanks for playing, {player.name}! You're walking away with ${player.current_winnings:,}!")
                break

            self.display.dramatic_reveal()

            if question.is_correct_answer(player_answer):
                player.update_winnings(question.prize_money)
                print(f"\nCorrect! You've won ${player.current_winnings:,}!")
                
                if question_number < len(self.questions):
                    print(f"\nDo you want to continue for ${self.questions[question_number].prize_money:,}?")
                    print("Press Enter to continue or 'Q' to quit: ")
                    if input().upper() == 'Q':
                        print(f"\nCongratulations! You're walking away with ${player.current_winnings:,}!")
                        break
                else:
                    print("\nCONGRATULATIONS! You've won the game and become a MILLIONAIRE!")
                    break
            else:
                print(f"\nSorry, that's incorrect! The correct answer was {question.correct_answer}.")
                print("Game Over!")
                player.reset_game()
                break

            question_number += 1
            time.sleep(GameConfig.DRAMATIC_PAUSE)

def main():
    """Main entry point of the game"""
    game_manager = GameManager()
    print("Please enter your name: ")
    player = Player(input().strip())
    
    while True:
        game_manager.play_game(player)
        print("\nWould you like to play again? (Y/N): ")
        if input().upper() != 'Y':
            print(f"\nThanks for playing, {player.name}! Goodbye!")
            break
        player.reset_game()

if __name__ == "__main__":
    main()