import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "games"))
sys.path.append(os.path.join(current_dir, "utils"))

from utils.typing_effect import typing_effect

# welcome screen

print("""Software not to be republished elsewhere. Harshit Khemani © 2024 (github.com/HKTITAN/)
----------------------------------------------------------------------

░█████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗░░░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░██╔══██╗╚██╗░██╔╝
███████║██████╔╝██║░░╚═╝███████║██║░░██║█████╗░░░░░██████╔╝░╚████╔╝░
██╔══██║██╔══██╗██║░░██╗██╔══██║██║░░██║██╔══╝░░░░░██╔═══╝░░░╚██╔╝░░
██║░░██║██║░░██║╚█████╔╝██║░░██║██████╔╝███████╗██╗██║░░░░░░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░

----------------------------------------------------------------------
""")

typing_effect("COMPUTER: Welcome to Arcade.py! 🎯\nWhat's your name? 😎\n")

username: str = input("""    >>> """)

if username == "":
    username = "Player"

elif not (username, str):
    username = "Player"

print("")
print("----------------------------------------------------------------------\n")

typing_effect(f"COMPUTER: Hey {username}! Let's get started! 🚀\n")

# game options
game_options = {
    1: "Rock Paper Scissors",
    2: "High Low",
    3: "Random Guesser"
    # add more games here
}

# game selection
print("""----------------------------------------------------------------------

Game Selection Menu:
""")

for option, game in game_options.items():
    print(f"    {option}. {game}")

print("""
    0. Exit

----------------------------------------------------------------------
""")

typing_effect("COMPUTER: Which game would you like to play today? 🤔\n")

game = None

while game not in game_options:
    game = input("    >>> ")
    print("")
    try:
        game = int(game)
        if game not in game_options and game != 0:
            print("Please enter a valid game option.")
    except ValueError:
        print("Please enter a valid integer.")

    if game == 0:
        print("----------------------------------------------------------------------\n")
        typing_effect("COMPUTER: Thanks for coming. Goodbye! 👋\n")
        print("----------------------------------------------------------------------\n")
        sys.exit()

game = game_options.get(game)

print("----------------------------------------------------------------------\n")
typing_effect(f"Loading {game}...\n")
print("----------------------------------------------------------------------\n")

if game == 1:
    from games.rockpaperscissors import rps
    rps()