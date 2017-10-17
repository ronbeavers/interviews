import pytest
import Blackjack


def test_instances(deck, dealer, player, card):
    assert isinstance(deck, Blackjack.Deck)
    assert isinstance(dealer, Blackjack.Hand)
    assert isinstance(player, Blackjack.Hand)
    assert isinstance(card, Blackjack.Card)

def test_outcome_tie():
    player = Blackjack.Hand()
    dealer = Blackjack.Hand()
    dealer.add_card(Blackjack.Card('S', '10'))
    dealer.add_card(Blackjack.Card('C', '8'))
    player.add_card(Blackjack.Card('H', '8'))
    player.add_card(Blackjack.Card('D', '10'))

    assert player.get_value() == dealer.get_value()
    print 'dealer: ' + str(dealer.get_value()), 'player: ' + str(player.get_value()), 'The hand is a tie'

def test_outcome_dealer():
    player = Blackjack.Hand()
    dealer = Blackjack.Hand()
    dealer.add_card(Blackjack.Card('S', '10'))
    dealer.add_card(Blackjack.Card('C', 'J'))
    player.add_card(Blackjack.Card('H', '4'))
    player.add_card(Blackjack.Card('D', '10'))

    assert player.get_value() < dealer.get_value()
    print 'dealer: ' + str(dealer.get_value()), 'player: ' + str(player.get_value()), 'dealer wins'

def test_outcome_player():
    player = Blackjack.Hand()
    dealer = Blackjack.Hand()
    dealer.add_card(Blackjack.Card('S', '5'))
    dealer.add_card(Blackjack.Card('C', '8'))
    player.add_card(Blackjack.Card('H', '7'))
    player.add_card(Blackjack.Card('D', '10'))

    assert player.get_value() > dealer.get_value()
    print 'dealer: ' + str(dealer.get_value()), 'player: ' + str(player.get_value()), 'player wins'

def test_hit(dealer, player, deck):
    player_before = len(player.hand)
    dealer_before = len(dealer.hand)
    player.hit(deck)
    dealer.hit(deck)
    player_after = len(player.hand)
    dealer_after = len(dealer.hand)

    assert player_after > player_before
    assert dealer_after > dealer_before
    print 'hits work'

def test_shuffle(deck):
    deck.shuffle()
    card1 = deck.deal_card()
    deck.shuffle()
    card2 = deck.deal_card()

    assert card1 != card2
    print 'shuffling works'

def test_ace():
    player = Blackjack.Hand()
    dealer = Blackjack.Hand()

    player.add_card(Blackjack.Card('S', 'A'))
    player.add_card(Blackjack.Card('H', '10'))
    dealer.add_card(Blackjack.Card('D', 'A'))
    dealer.add_card(Blackjack.Card('C', 'A'))

    assert player.get_value() > dealer.get_value()
    assert player.get_value() == 21
    assert dealer.get_value() == 12
    print 'dealer: ' + str(dealer.get_value()), 'player: ' + str(player.get_value()), 'Ace test complete'



def main():
    deck = Blackjack.Deck()
    dealer = Blackjack.Hand()
    player = Blackjack.Hand()
    card = Blackjack.Card('S', '5')
    test_instances(deck, dealer, player, card)
    test_outcome_dealer()
    test_outcome_player()
    test_outcome_tie()
    test_ace()
    test_hit(dealer, player, deck)
    test_shuffle(deck)

if __name__ == '__main__':
    main()