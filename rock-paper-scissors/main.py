import random

choices = ["rock", "paper", "scissors"]
winners = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
while True:
    start_game = input("(P)lay or (Q)uit?")
    if start_game == 'Q' or start_game == "q":
        print("Goodbye")
        break
    else:
        while True:
            computer_choice = random.choice(choices)
            player_choice = input("Pick rock, paper, or scissors:")
            if player_choice not in choices:
                print("Please enter a valid choice")
            else:
                print("Computer chose:", computer_choice)
                print("Player chose:", player_choice)
                if player_choice == computer_choice:
                    winner = "Draw"
                    print(winner)
                elif player_choice == winners[computer_choice]:
                    winner = "Computer wins!"
                    print(winner)
                elif computer_choice == winners[player_choice]:
                    winner = "Player wins!"
                    print(winner)
            ans = input("Do you want to play again? (y/n)?")
            if ans == 'n' or ans == 'N':
                break