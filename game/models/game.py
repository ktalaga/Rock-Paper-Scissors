from random import choice
class Game():

    def play_game(self, player_1, player_2):

        if player_1.choice == "scissors" and player_2.choice == "paper":
            return "Player 1 won by playing scissors"

        if player_1.choice == "paper" and player_2.choice == "scissors":
            return "Player 2 won by playing scissors"

        elif player_1.choice == "scissors" and player_2.choice == "rock":
            return "Player 2 won by playing rock"

        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return "Player 1 won by playing rock"

        elif player_1.choice == "paper" and player_2.choice == "rock":
            return "Player 1 won by playing paper"

        elif player_1.choice == "rock" and player_2.choice == "paper":
            return "Player 2 won by playing paper"

        elif player_1.choice == "rock" and player_2.choice == "rock":
            return "This is a draw. Play again!"

        elif player_1.choice == "paper" and player_2.choice == "paper":
            return "This is a draw. Play again!"

        elif player_1.choice == "scissors" and player_2.choice == "scissors":
            return "This is a draw. Play again!"       
        
        else:
            return "Wrong input. Please choose paper, rock or scissors! Monkeys and bananas are not allowed"





class Computer():
    def __init__(self, choice):
        self.choice = choice(["paper", "rock", "scissors"])