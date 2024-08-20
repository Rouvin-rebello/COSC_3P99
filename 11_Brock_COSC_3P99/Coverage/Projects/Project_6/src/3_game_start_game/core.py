import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def start_game(self, restart=False):
    self.set_mode(0)
    self.init_game()
    self.init_players_in_map()
    self.player.set_vel_to_zero()
    self.game_loop()