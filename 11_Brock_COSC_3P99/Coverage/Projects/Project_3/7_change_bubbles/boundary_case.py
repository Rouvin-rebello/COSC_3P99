import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def change_bubbles(self):
        if self.colors_count > 1:
            self.colors_count -= 1