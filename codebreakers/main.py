import random

'''RULES :
 - 4 color code
 - 10 guesses
 - 6 colors to choose from
 - Hints ?'''

game_options = ["P", "Q", "p", "q"]
colors = ["red", "blue", "green", "cyan", "magenta", "yellow"]
rounds = 10
total_rounds = 0
secret_code = []
myguess = None
code_length = 4
correct_guess = []


def win_game(secret, guess):
    if guess == secret:
        return True


def my_guess(length):
    my_code = []
    while length > 0:
        guess = input("Pick a color: ")
        if guess not in colors:
            print("Please choose a valid color.")
        else:
            my_code.append(guess)
            length -= 1
    return my_code


def hint(secret, guess):
    correct_count = 0
    incorrect_count = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            correct_count += 1
        else:
            incorrect_count += 1
    return "You guessed {0} correct and {1} incorrect".format(correct_count, incorrect_count)


while True:
    start_game = input("(P)lay or (Q)uit? ")
    if start_game not in game_options:
        print("Not a valid option. Please try again.")
    elif start_game == "Q":
        print("Closing game... Goodbye")
        break
    else:
        while code_length > 0:
            secret_code.append(random.choice(colors))
            code_length -= 1
        else:
            print("Secret code has been created")
        while True:
            valid_choices = ["1", "2", "3", "4"]
            game_choice = input("[1] Make a guess\n"
                                "[2] See guess\n"
                                "[3] See hint\n"
                                "[4] Back to Menu\n"
                                "[5] Quit game\n"
                                "What would you like to do? ")
            if game_choice not in valid_choices:
                print("Please choose a valid menu option")
            elif game_choice == "1":
                code_length = 4
                while total_rounds < 10:
                    if total_rounds > 8:
                        print("2 rounds remaining!")
                    total_rounds += 1
                    myguess = my_guess(code_length)
                    if win_game(secret_code, myguess):
                        game_over = input("You win! Would you like to try again (y/n)? ")
                        if game_over == "n":
                            break
                    elif not win_game(secret_code, myguess):
                        rounds_left = 10 - total_rounds
                        print("Not quite! You have {0} guess remaining".format(rounds_left))
                        break
                else:
                    print("Game over! The code was {0}. You didn't guess it correctly in time. "
                          "Try again (y/n)? ".format(secret_code))
                    break
            elif game_choice == "2":
                if myguess is None:
                    print("You haven't made a guess yet! Make a guess and then try again")
                else:
                    print(myguess)
            elif game_choice == "3":
                if myguess is None:
                    print("You haven't made a guess yet! Make a guess and then try again")
                else:
                    my_hint = hint(secret_code, myguess)
                    print(my_hint)
            elif game_choice == "4":
                break
            else:
                quit()

