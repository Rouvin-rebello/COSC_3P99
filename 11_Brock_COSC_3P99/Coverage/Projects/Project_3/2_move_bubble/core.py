import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def move_bubble(self, move_to):
    self.bubble.rect.centerx = move_to.center.x
    self.bubble.rect.centery = move_to.center.y
    move_to.bubble = self.bubble
    self.bubble = None

