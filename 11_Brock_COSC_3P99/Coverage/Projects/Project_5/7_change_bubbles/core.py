import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def change_bubbles(self):
    self.bubbles = random.sample(BUBBLES, self.colors_count)
    self.next_bullet = None
    self.charge()