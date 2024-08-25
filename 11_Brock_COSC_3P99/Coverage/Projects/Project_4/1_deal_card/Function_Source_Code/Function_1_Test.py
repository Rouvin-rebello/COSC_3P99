from unittest import TestCase, main
from Function_1_Source import deal_card

class DealCardTest(TestCase):
    def test_deal_card_type(self):
        self.assertIsInstance(deal_card(), int)

    def test_deal_card_value(self):
        card = deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    main()
