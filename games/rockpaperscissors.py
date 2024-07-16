import random
from arcade.utils.typing_effect import typing_effect

def rps():
    print("test message")
    rps_choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
    }
    
    rps_user_choice = None
    
    typing_effect("""Let's play Rock Paper Scissors!
Here are your Choices:
    """)
    for option, rps_user_choice in rps_choices.items():
        print(f"    {option}. {rps_user_choice}")
    
    print("""
----------------------------------------------------------------------

Choose:
""")
    rps_user_choice: int = input("    >>> ")
    
rps()