from blackjack.deck import Deck

def main():

    deck = Deck()                   # Creates a random deck
    hand = []                       # Keeps track of the players cards
    dealerhand = []                 # Keeps track of the dealers cards
    playerace = 0                   # Keeps count of number of aces player has pulled
    dealerace = 0                   # Keeps count of number of aces player has pulled

    # Dealer pulls first card
    card = deck.cards.pop()             # Pulls first random card
    dealerhand.append(card)             # Adds card to dealers cards
    if (card.rank.value == 1):          # if card is Ace
        dealerrank = card.rank.name     # Show Ace as card name
        dealerace += 1                  # Add one to dealer ace counter
    elif (card.rank.value > 10):        # if card is picture card
        dealerrank = card.rank.name     # Show cards enum name
    else:
        dealerrank = card.rank.value    # else show cards number

    dealersuit = card.suit.name         # Saves the suit of the card for later
    dealertotal = sum([min(card.rank.value, 10) for card in dealerhand]) + (dealerace*10)   # shows the total of dealer
    print(f'\nDealer pulled {dealerrank} of {dealersuit}.\n')   # Prints out what dealer pulled

    # Players turn to play
    while True:
        read = input('Stand, Hit:\n')       # Asks if player wants to hit or stand
        if read == 'Hit' or read == 'h':
            card = deck.cards.pop()         # if hit pulls the next card in the deck
            hand.append(card)               # Adds card to player hand

            total = sum([min(card.rank.value, 10) for card in hand])    # sums up the value of the cards

            if playerace > 0 and total < 12:  # if dealer has ace and total is less than 12 add 10 to total
                total += 10

            if (card.rank.value == 1):      # if card is Ace
                showcard = card.rank.name   # Show Ace as card name
                playerace += 1              # Add one to player ace counter
            elif (card.rank.value > 10):    # if card is picture card
                showcard = card.rank.name   # Show cards enum name
            else:
                showcard = card.rank.value  # else show cards number

            if(total < 21):     # if total less than 21 show cards and let player continue to play
                print(f'\nHit with {showcard} of {card.suit.name}. Your total is {total}\n'
                      f'Dealer has {dealerrank} of {dealersuit}.')
            elif(total == 21):  # if total is 21 show cards and end player turn
                print(f'\nHit with {showcard} of {card.suit.name}. Your total is 21!\nYou hit BlackJack!')
                break
            else:               # if total over 21 show cards and end player turn
                print(f"\nHit with {showcard} of {card.suit.name}. Your total is {total}\n"
                      f"You are over 21. That's a bust")
                break
        elif read == 'Stand' or read == 's':    # if player chooses stand end players turn
            break

    # Dealers turn to play
    # dealer hits until they have 17 or greater, dealer ends the game if the player busts
    while (dealertotal < 17 and total < 22):
        card = deck.cards.pop()             # Pull top card from deck
        dealerhand.append(card)             # Add card to dealer hand

        dealertotal = sum([min(card.rank.value, 10) for card in dealerhand])    # sums up the value of the cards
        if dealerace > 0 and dealertotal < 12:  # if dealer has ace and total is less than 12 add 10 to total
            dealertotal += 10

        if (card.rank.value == 1):          # if card is Ace
            showcard = card.rank.name     # Show Ace as card name
            dealerace += 1                  # Add one to dealer ace counter
        elif (card.rank.value > 10):        # if card is picture card
            showcard = card.rank.name     # Show cards enum name
        else:
            showcard = card.rank.value    # else show cards number

        if (dealertotal < 21):      # if total less than 21 show cards and let dealer continue to hit
            print(f'\nDealer hit with {showcard} of {card.suit.name}. Dealers total is {dealertotal}\n'
                  f'Your total is {total}.')
        elif (dealertotal == 21):   # if total is 21 show cards and end game
            print(f'\nDealer hit with {showcard} of {card.suit.name}. Dealers total is 21!\nDealer hit BlackJack!'
                  f'\nYour total is {total}.')
            break
        else:                       # if total over 21 show cards and end game
            print(f"\nDealer hit with {showcard} of {card.suit.name}. Dealers total is {dealertotal}\n"
                  f"Dealer is over 21. That's a bust")
            break

    # Show results from game
    # print(f'You had a total of {total}, dealer had a total of {dealertotal}')
    if total > 21:
        print('You Lost!')
    elif dealertotal > 21:
        print('You Won!')
    elif total > dealertotal:
        print('You Won!')
    elif total < dealertotal:
        print('You Lost!')
    else:
        print('You tied!')


if __name__ == '__main__':
    main()
