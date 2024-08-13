from pybubble_shooter import *

def move_bubble(self, move_to):
    if not move_to.bubble:  # Ensures that move_to does not already contain a bubble (edge case)
        print("Here")