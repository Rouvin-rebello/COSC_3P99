import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def check_ghosts_state(self):
        if self.is_at_least_a_ghost_vulnerable():
            if self.ghosts_timer == 360:
                self.set_mode(GameMode.normal)
                for ghost in self.ghosts:
                    ghost.set_normal()
            else:
                self.ghosts_timer += 1
