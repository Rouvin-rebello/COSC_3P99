# File: Function_Test.py

try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise


from unittest import TestCase
from Function_Core_Functionality import DeckOfCards as CoreDeckOfCards
from Function_Boundary_Conditions import DeckOfCards as BoundaryDeckOfCards
from Function_Error_Handling import DeckOfCards as ErrorDeckOfCards
from Function_Integration_Points import DeckOfCards as IntegrationDeckOfCards
from Function_Output_Consistency import DeckOfCards as OutputDeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        # Create decks for testing
        self.core_deck = CoreDeckOfCards([i for i in range(52)])
        self.boundary_deck_empty = BoundaryDeckOfCards([])
        self.boundary_deck_single = BoundaryDeckOfCards([1])
        self.error_deck_invalid = [1, 2, 3]
        self.integration_deck = IntegrationDeckOfCards([i for i in range(52)])
        self.output_deck = OutputDeckOfCards([i for i in range(52)])

    # Test Core Functionality
    def test_core_functionality(self):
        shuffled_deck = self.core_deck.deck_of_cards.copy()
        self.core_deck.cards_shuffle()
        self.assertNotEqual(shuffled_deck, self.core_deck.deck_of_cards)

    # Test Boundary Conditions and Edge Cases
    def test_boundary_conditions(self):
        self.boundary_deck_empty.cards_shuffle()
        self.assertEqual(len(self.boundary_deck_empty.deck_of_cards), 0)

        self.boundary_deck_single.cards_shuffle()
        self.assertEqual(len(self.boundary_deck_single.deck_of_cards), 1)

    # Test Error Handling
    def test_error_handling(self):
        with self.assertRaises(TypeError):
            ErrorDeckOfCards(self.error_deck_invalid)

    # Test Integration Points
    def test_integration_points(self):
        self.integration_deck.cards_shuffle()
        self.assertEqual(len(self.integration_deck.deck_of_cards), 52)

    # Test Output Consistency
    def test_output_consistency(self):
        original_length = len(self.output_deck.deck_of_cards)
        self.output_deck.cards_shuffle()
        self.assertEqual(len(self.output_deck.deck_of_cards), original_length)

if __name__ == '__main__':
    TestCase.main()
