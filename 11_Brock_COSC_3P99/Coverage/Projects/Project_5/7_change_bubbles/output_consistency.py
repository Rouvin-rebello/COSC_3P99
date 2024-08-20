import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def change_bubbles(self):
    if len(self.bubbles) <= 2:
            self.delete_bubbles()
            self.create_bubbles(10)
    else:
        self.increase_bubbles(10)