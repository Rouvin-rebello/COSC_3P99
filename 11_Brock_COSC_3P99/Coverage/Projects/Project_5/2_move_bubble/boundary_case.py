import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def move_bubble(self, move_to):
    if not move_to.bubble:  # Ensures that move_to does not already contain a bubble (edge case)
        print("Here")