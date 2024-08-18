import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacman import *

def draw(self, screen, game_mode):
    if game_mode == GameMode.game_over:
        return False