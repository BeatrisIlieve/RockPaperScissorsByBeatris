# importing colorama module in order to add colours and style to the text
import colorama
from colorama import Fore, Back, Style

# importing random module so as the computer can play a move
import random

# welcoming the user and printing the instructions of the game
print(f"{' ' * 8}" f"{Style.BRIGHT}{Fore.BLUE}'{Fore.MAGENTA}W{Fore.YELLOW}e{Fore.GREEN}l{Fore.MAGENTA}c{Fore.YELLOW}o"
      f"{Fore.GREEN}m{Fore.MAGENTA}e {Fore.YELLOW}t{Fore.BLUE}o {Fore.MAGENTA}R{Fore.GREEN}o"
      f"{Fore.BLUE}c{Fore.MAGENTA}k, {Fore.YELLOW}p{Fore.GREEN}a{Fore.MAGENTA}p{Fore.YELLOW}e"
      f"{Fore.GREEN}r {Fore.MAGENTA}a{Fore.YELLOW}n{Fore.GREEN}d {Fore.YELLOW}s{Fore.MAGENTA}c"
      f"{Fore.GREEN}i{Fore.BLUE}s{Fore.MAGENTA}s{Fore.YELLOW}o{Fore.BLUE}r{Fore.GREEN}s "
      f"{Fore.GREEN}g{Fore.BLUE}a{Fore.MAGENTA}m{Fore.YELLOW}e{Fore.BLUE}'")
print()

# auxiliary variables
wins_counter = 0
draws_counter = 0
loses_counter = 0
current_loses_counter = 0

# taking user input
user_name = input(Fore.CYAN + 'Enter your name: ')
print(Fore.MAGENTA + f'{Fore.MAGENTA}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O '
                     f'{Fore.CYAN}{user_name}! It\'s your turn.')

# looping until the user enters an invalid input
while True:
    player_choice = input(Fore.CYAN + f'Choose {Fore.BLACK}[r]{Fore.CYAN}ock, {Fore.BLACK}[p]{Fore.CYAN}aper '
                                      f'or {Fore.BLACK}[s]{Fore.CYAN}cissors: ')

    # initializing the value of the user choice
    if player_choice == 'r':
        player_choice = 'rock'
    elif player_choice == 'p':
        player_choice = 'paper'
    elif player_choice == 's':
        player_choice = 'scissors'
    else:
        # case of invalid input
        raise SystemExit('Invalid input. Try again...')

    # the random module randomly chooses a str in the choice_list list and assigns it to computer_choice
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)

    # loss condition
    if player_choice == 'scissors' and computer_choice == 'rock' or \
                    player_choice == 'rock' and computer_choice == 'paper' or \
                    player_choice == 'paper' and computer_choice == 'scissors':
        # if a user loses two times, variables are being swapped so that the user wins on the third time
        current_loses_counter += 1
        if current_loses_counter == 2:
            player_choice, computer_choice = computer_choice, player_choice
            wins_counter += 1
            current_loses_counter = 0
            print(Fore.GREEN + f'{Style.BRIGHT}{user_name}, you win!')
        else:
            loses_counter += 1
            print(Fore.RED + f'{Style.BRIGHT}{user_name} you lose!')
    # draw condition
    elif player_choice == computer_choice:
        draws_counter += 1
        print(Fore.YELLOW + f'{Style.BRIGHT}Draw!')
    # win condition
    else:
        wins_counter += 1
        print(Fore.GREEN + f'{Style.BRIGHT}{user_name}, you win!')

    # printing the user's choice
    print(Fore.MAGENTA + f"{user_name}'s choice is {player_choice}.")
    # printing computer choice
    print(Fore.BLUE + f'The computer choice is {computer_choice}.')

    # giving the user options to continue playing or exit the game
    next_choice = input(Fore.CYAN + f'{Style.NORMAL}If you want to play again, press {Fore.BLACK}[y]{Fore.CYAN}, '
                                    f'if not press {Fore.BLACK}[n]{Fore.CYAN}: ')

    # if user's choice is 'n', we break the while loop
    if next_choice == 'n':
        print(f'{Style.BRIGHT}{Fore.MAGENTA}T{Fore.GREEN}h{Fore.BLUE}a{Fore.YELLOW}n{Fore.GREEN}k{Fore.MAGENTA}'
              f' y{Fore.BLUE}o{Fore.MAGENTA}u {Fore.BLUE}f{Fore.RED}o{Fore.MAGENTA}r p{Fore.BLUE}l'
              f'{Fore.RED}a{Fore.GREEN}y{Fore.YELLOW}i{Fore.BLUE}n{Fore.MAGENTA}g,{Fore.MAGENTA} {Fore.CYAN}{user_name}!')
        # printing final result of the games
        print(Fore.GREEN + f'{Back.LIGHTWHITE_EX}Wins: {wins_counter}')
        print(Fore.YELLOW + f'{Back.LIGHTWHITE_EX}Draws: {draws_counter}')
        print(Fore.RED + f'{Back.LIGHTWHITE_EX}Loses: {loses_counter}')
        break

    # case of invalid input
    if next_choice != 'n' and next_choice != 'y':
        raise SystemExit('Invalid input. Try again...')
