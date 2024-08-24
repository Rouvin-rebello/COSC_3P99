from DeckOfCards import DeckOfCards
from Function_11_Core import set_hand_core
from Function_11_Boundary import set_hand_boundary
from Function_11_ErrorHandling import set_hand_error_handling

def set_hand_integration(player, deck):
    set_hand_boundary(player, deck)
    set_hand_error_handling(player, deck)
    return set_hand_core(player, deck)
