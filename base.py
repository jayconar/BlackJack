from tkinter import Tk, Canvas, Button
from interface import interface
from game import *

BG = "#35654d"
FONT = ("Franklin Gothic Demi", 13)


def main():
    screen = Tk()  # Creating the main screen
    screen.title("BlackJack")
    screen.iconbitmap(default=deck['ICON'])
    screen.geometry("900x700")  # Screen size set to accommodate the maximum cards possible in a single hand (i.e. 11)

    dealer_canvas = Canvas(screen, bg=BG, height=300, width=900, highlightthickness=0)
    player_canvas = Canvas(screen, bg=BG, height=300, width=900, highlightthickness=0)

    bicycle = PhotoImage(file=deck['CARD_BACK'])
    face_down = dealer_canvas.create_image(420, 150, image=bicycle)  # Updating face_down

    def new_game():
        nonlocal face_down  # To modify the global face_down variable
        dealer_canvas.delete(face_down)  # Deleting the face-down card in the dealer canvas
        dealer_canvas.delete("all")  # Clearing the dealer's cards
        dealer_canvas.update()  # Updating the dealer's canvas
        face_down = dealer_canvas.create_image(420, 150, image=bicycle)  # Recreating the face-down card after deletion

        # Clearing the player's cards
        player_canvas.delete("all")  # Deleting all objects on the player canvas
        player_canvas.update()  # Updating the player canvas

        # Resetting the player card position to its initial position
        player_spot[0] = 420

        player_hand.clear()  # Clearing player's hand
        dealer_hand.clear()  # Clearing dealer's hand

        # Resetting the dealer card position to its initial position
        dealer_spot[0] = 540

        # Dealing new hands
        player_hand.extend([deal(), deal()])
        dealer_hand.extend([deal(), deal()])
        display(dealer_canvas, deck[dealer_hand[1]], x=480, y=150)
        for carte in player_hand:
            display(player_canvas, deck[carte], x=player_spot[0], y=player_spot[1])
            player_spot[0] += 60
        if hand_value(player_hand) == 21 or hand_value(dealer_hand) == 21:  # Checking for BlackJack
            stand(hit_button, player_hand, dealer_hand, dealer_canvas, face_down, blackjack=1)
        else:  # Enabling Hit and Stand buttons
            hit_button.config(state="normal")
            stand_button.config(state="normal")

    # Calling the function to create the Blackjack interface
    player_hand = [deal(), deal()]
    dealer_hand = [deal(), deal()]
    interface(screen, dealer_canvas, player_canvas)
    display(dealer_canvas, deck[dealer_hand[1]], x=480, y=150)
    for card in player_hand:
        display(player_canvas, deck[card], x=player_spot[0], y=player_spot[1])
        player_spot[0] += 60
    stand_button = Button(text="Stand", bg="black", fg="white", width=8, font=FONT,
                          command=lambda: stand(hit_button, player_hand, dealer_hand, dealer_canvas, face_down))
    stand_button.grid(row=2, column=2)
    hit_button = Button(text="Hit", bg="black", fg="white", width=8, font=FONT,
                        command=lambda: hit(player_hand, dealer_hand, player_canvas, dealer_canvas,
                                            hit_button, face_down))
    hit_button.grid(row=2, column=0)
    new_game_button = Button(text="New Game", bg="black", fg="white", width=14, font=FONT, command=new_game)
    new_game_button.grid(row=3, column=1)
    if hand_value(player_hand) == 21 or hand_value(dealer_hand) == 21:
        stand(hit_button, player_hand, dealer_hand, dealer_canvas, face_down, blackjack=1)

    screen.mainloop()
