import random
from tkinter import PhotoImage, messagebox
from deck import deck
from interface import display, image_list

player_spot = [420, 150]
dealer_spot = [540, 150]


def deal():
    """Returns a random card every single time it's called"""
    while True:
        card = random.choice(list(deck.keys()))
        if card not in {"CARD_BACK", "ICON"}:  # Excluding the face down and icon
            return card


def hand_value(hand):
    """Returns the hand value and adjusts value for Ace based on current hand value"""
    t_var = []
    for card in hand:
        if card[0] in ('J', 'K', 'Q'):
            t_var.append(10)
        elif card[0].isdigit():
            t_var.append(int(''.join([char for char in card if char.isdigit()])))
    for card in hand:
        if card[0] == 'A':
            if sum(t_var) < 11:
                t_var.append(11)
            else:
                t_var.append(1)
    return sum(t_var)


def hit(player_hand, dealer_hand, player_canvas, dealer_canvas, hit_button, face_down):
    """"Adds a new card to the hand as long as the user is not bust and wants to play"""
    if hand_value(player_hand) < 21:
        card = deal()
        player_hand.append(card)
        display(player_canvas, deck[card], x=player_spot[0], y=player_spot[1])
        player_spot[0] += 60
    if hand_value(player_hand) >= 21:
        stand(hit_button, player_hand, dealer_hand, dealer_canvas, face_down)


def stand(hit_button, player_hand, dealer_hand, dealer_canvas, face_down, blackjack=0):
    """Finalizes hands and calls result on them"""
    hit_button.config(state="disabled")
    face_up = PhotoImage(file=deck[dealer_hand[0]])
    image_list.append(face_up)
    dealer_canvas.itemconfig(face_down, image=face_up)
    if blackjack == 0:
        dealer(dealer_hand, dealer_canvas)
    result(player_hand, dealer_hand)


def dealer(dealer_hand, canvas):
    """Gets cards for the dealer"""
    if hand_value(dealer_hand) < 17:
        card = deal()
        dealer_hand.append(card)
        display(canvas, deck[card], x=dealer_spot[0], y=dealer_spot[1])
        dealer_spot[0] += 60
        dealer(dealer_hand, canvas)


def result(player_hand, dealer_hand):
    """Determines win, lose, or tie and displays a message box."""
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    stats = f"Your hand: {player_value}\nDealer's hand: {dealer_value}"

    if player_value > 21 or (player_value < dealer_value < 22):
        messagebox.showinfo("Result", f'You lose\n{stats}')
    elif player_value == dealer_value:
        messagebox.showinfo("Result", f'It\'s a push\n{stats}')
    elif player_value > dealer_value or dealer_value > 21:
        messagebox.showinfo("Result", f'You win!\n{stats}')
