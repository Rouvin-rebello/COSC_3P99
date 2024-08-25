from unittest import TestCase
from Function_8_Source import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        # Create two decks with identical card sequences for comparison after shuffling
        self.deck1 = DeckOfCards([i for i in range(52)])
        self.deck2 = DeckOfCards([i for i in range(52)])

    def test_cards_shuffle(self):
        # Shuffle deck2 and compare it with deck1 to ensure they're different after shuffle
        self.deck2.cards_shuffle()

        # Assert that the decks are not equal after shuffling
        self.assertNotEqual(self.deck1.deck_of_cards, self.deck2.deck_of_cards)
