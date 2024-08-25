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

class MockCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class TestDeckOfCards(TestCase):
    def setUp(self):
        # Create mock decks for testing
        self.core_deck = CoreDeckOfCards([MockCard(i + 1, 1) for i in range(13)])
        self.boundary_deck = BoundaryDeckOfCards([MockCard(i + 1, 1) for i in range(13)])
        self.error_deck_invalid = [1, 2, 3]
        self.integration_deck = IntegrationDeckOfCards([MockCard(i + 1, 1) for i in range(13)])
        self.output_deck = OutputDeckOfCards([MockCard(i + 1, 1) for i in range(13)])

    # Test Core Functionality
    def test_core_functionality(self):
        dealt_card = self.core_deck.deal_one()
        self.assertEqual(len(self.core_deck.deck_of_cards), 12)
        self.assertNotIn(dealt_card, self.core_deck.deck_of_cards)

    # Test Boundary Conditions and Edge Cases
    def test_boundary_conditions(self):
        with self.assertRaises(ValueError):
            empty_deck = BoundaryDeckOfCards([])
            empty_deck.deal_one()

    # Test Error Handling
    def test_error_handling(self):
        with self.assertRaises(TypeError):
            ErrorDeckOfCards(self.error_deck_invalid)

    # Test Integration Points
    def test_integration_points(self):
        dealt_card = self.integration_deck.deal_one()
        self.assertIsInstance(dealt_card, MockCard)

    # Test Output Consistency
    def test_output_consistency(self):
        original_length = len(self.output_deck.deck_of_cards)
        self.output_deck.deal_one()
        self.assertEqual(len(self.output_deck.deck_of_cards), original_length - 1)

if __name__ == '__main__':
    TestCase.main()
