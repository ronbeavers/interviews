import random


#globals for blackjack and cards
outcome = ""
current = ""
dealer = []
player = []
deck = {}
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# define card class
class Card:
    def __init__(self, suit, rank):
        #Assign suit and rank to card
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

        #Assign values to the cards based on rank
        if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.cardValue = int(rank)
        elif rank in ['J', 'Q', 'K']:
            self.cardValue = 10
        elif rank == 'A':
            self.cardValue = 11
        else:
            self.cardValue = None
            print "Invalid card value: ", rank

    def __str__(self):
        return self.suit + self.rank

    #Convert and return suit to String name value
    def get_suit(self):
        if self.suit == 'S':
            self.suit = 'Spades'
            return self.suit
        elif self.suit == 'C':
            self.suit = 'Clubs'
            return self.suit
        elif self.suit == 'D':
            self.suit = 'Diamonds'
            return self.suit
        elif self.suit == 'H':
            self.suit = 'Hearts'
            return self.suit
        else:
            self.suit = None
            print "Invalid suit"

    #Convert and return rank to String name value
    def get_rank(self):
            if self.rank == 'J':
                self.rank = 'Jack'
                return self.rank
            elif self.rank == 'Q':
                self.rank = 'Queen'
                return self.rank
            elif self.rank == 'K':
                self.rank = 'King'
                return self.rank
            elif self.rank == 'A':
                self.rank = 'Ace'
                return self.rank
            else:
                return self.rank

    def get_value(self):
        return self.cardValue

#Define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def show_cards(self):
        return ', '.join([card.get_rank() + " of " + card.get_suit() for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    #Determine if the Ace is a 1 or an 11
    def get_value(self):
        sum = 0
        ace = False
        for card in self.hand:
            sum += card.get_value()
            if card.get_rank() == 'Ace':
                ace = True
        if ace and sum > 21:
            return sum - 10
        else:
            return sum

    def hit(self, deck):
        self.add_card(deck.deal_card())

    def busted(self):
        global busted
        sum = self.get_value()
        if sum > 21:
            return True

#Define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        self.shuffle()

    #add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card


#Define the actions for events from cli
def deal():
    global outcome, current, dealer, player, deck
    deck = Deck()
    dealer = Hand()
    player = Hand()
    outcome = ""
    current = "New deal? "
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)
    print "Dealer initially has "+ dealer.show_cards() +" with the value of "+str(dealer.get_value())
    print "Player initially has "+player.show_cards()+" with the value of "+str(player.get_value())
    #Prompt the player for a hit
    while player.get_value() <= 21 and not player.busted():
        if player.get_value() == 21:
            stand()
        player_hit = raw_input("Player has " +str(player.get_value()) + " Do you want a hit? Y/N ").lower()
        if player_hit == 'y':
            player.hit(deck)
            print "Player has "+str(player.get_value())
        else:
            stand()
    new_deal = raw_input(current).lower()
    if new_deal == 'y':
        deal()
    else:
        exit()

def stand():
    global outcome, current
    #repeatedly hit dealer until his hand has value 17 or more
    while dealer.get_value() < 17:
        dealer.hit(deck)
        print "Dealer has " +str(dealer.get_value())
        if dealer.busted():
            outcome = "Dealer went bust! You won."
            print outcome
    #assign a message to outcome
    if not dealer.busted() and dealer.get_value() > player.get_value():
        outcome = "Dealer won."
        print outcome
    if not dealer.busted() and dealer.get_value() == player.get_value():
        outcome = "It's a tie."
        print outcome
    if not dealer.busted() and dealer.get_value() < player.get_value():
        outcome = "You won."
        print outcome
    current = "New deal? "
    new_deal = raw_input(current)
    if new_deal == 'Y'.lower():
        deal()
    else:
        exit()

def main():
    deal()

if __name__ == '__main__':
    main()