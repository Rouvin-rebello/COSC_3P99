from unittest import TestCase, main
from Function_1_Core_Functionality import core_deal_card
from Function_1_Boundary_Edge_Cases import boundary_deal_card
from Function_1_Error_Handling import error_handling_deal_card
from Function_1_Integration import integration_deal_card
from Function_1_Output_Consistency import consistent_deal_card

class DealCardTest(TestCase):
    def test_core_deal_card_type(self):
        self.assertIsInstance(core_deal_card(), int)

    def test_core_deal_card_value(self):
        card = core_deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_boundary_deal_card_value(self):
        card = boundary_deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_error_handling_deal_card_value(self):
        card = error_handling_deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_integration_deal_card_value(self):
        card = integration_deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_consistent_deal_card_value(self):
        card = consistent_deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    main()
