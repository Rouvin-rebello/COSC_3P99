import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def start_game(self, restart=False):
    if restart:
        self.maze.reinit_map()
        self.player.lives = 3