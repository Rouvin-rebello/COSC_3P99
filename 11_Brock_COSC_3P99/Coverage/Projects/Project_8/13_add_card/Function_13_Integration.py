from Function_13_Core import add_card_core
from Function_13_Boundary import add_card_boundary
from Function_13_ErrorHandling import add_card_error_handling

def add_card_integration(player, card):
    add_card_error_handling(player, card)
    add_card_boundary(player, card)
    return add_card_core(player, card)
