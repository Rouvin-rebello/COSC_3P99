from Function_12_Core import get_card_core
from Function_12_Boundary import get_card_boundary
from Function_12_ErrorHandling import get_card_error_handling

def get_card_integration(player):
    get_card_error_handling(player)
    get_card_boundary(player)
    return get_card_core(player)
