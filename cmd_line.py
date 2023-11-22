import random


# Two decks in this game
deck = [
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace",
    "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace"
          ]


def hand():
    """Returns a random card every single time"""
    return random.choice(deck)


def hand_value(the_hand):
    """Returns the hand value and adjusts value for Ace based on current hand value"""
    t_var = []
    for card in the_hand:
        if card != 'Ace' and type(card) == str:
            t_var.append(10)
        elif type(card) == int:
            t_var.append(card)
    for card in the_hand:
        if card == 'Ace':
            if sum(t_var) < 11:
                t_var.append(11)
            else:
                t_var.append(1)
    return sum(t_var)


def hit():
    """"Adds a new card to the hand as long as the user is not bust and wants to play"""
    hit_one = input('Do you want to hit? y/n\n')
    if hit_one == 'y':
        my_hand.append(hand())
        print(f"Your current hand: [{'  '.join(str(n) for n in my_hand)}] ({hand_value(my_hand)})")
        if hand_value(my_hand) < 21:
            hit()


def dealer():
    """Gets cards for the dealer"""
    if hand_value(dealer_hand) < 17:
        dealer_hand.append(hand())
        dealer()


def result():
    """Determines win, lose or tie"""
    stats = f"Your hand: [{'  '.join(str(n) for n in my_hand)}] ({my_value})\n"\
            f"Dealer's hand: [{'  '.join(str(n) for n in dealer_hand)}] ({dealer_value})"
    if my_value > 21 or (my_value < dealer_value < 22):
        print(f'You lose\n{stats}\n')
    elif my_value == dealer_value:
        print(f'It\'s a push\n{stats}\n')
    elif my_value > dealer_value or dealer_value > 21:
        print(f'You win!\n{stats}\n')


input('Enter any key to begin\n')
go = 'y'
while go == 'y':
    my_hand = [hand(), hand()]
    dealer_hand = [hand(), hand()]
    print(f'Your hand: [{my_hand[0]}  {my_hand[1]}] ({hand_value(my_hand)})')
    print(f'The dealer\'s hand: [{dealer_hand[0]}  Hidden]')
    if hand_value(my_hand) == 21 and my_hand != hand_value(dealer_hand):
        print('Blackjack! You win!')

    else:
        dealer()
        hit()
        my_value = hand_value(my_hand)
        dealer_value = hand_value(dealer_hand)
        result()

    go = input('Do you want to play again? y/n \n')
