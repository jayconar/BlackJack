import os

# Getting the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Creating a dictionary to map card names to their image file paths
deck = {}
suits = ['diamonds', 'hearts', 'clubs', 'spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

card_back_path = os.path.join(script_directory, 'art', 'card_back.png')
deck['CARD_BACK'] = card_back_path
icon = os.path.join(script_directory, 'art', 'blackjack.ico')
deck['ICON'] = icon

for suit in suits:
    for value in cards:
        card_name = f"{value[0] if len(value) > 2 else value}{suit[0]}".upper()
        image_path = os.path.join(script_directory, f'art', f'{value}_of_{suit}.png')
        deck[card_name] = image_path
# print(deck)
