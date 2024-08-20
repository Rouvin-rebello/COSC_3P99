import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacman import *

def draw(self, screen, game_mode):
    if game_mode in [GameMode.normal, GameMode.change_ghosts, GameMode.wait_after_eating_ghost]:
        if not self.vel_x == 0 or not self.vel_y == 0:
            self.anim_frame += 1

        if self.anim_frame == 9:
            self.anim_frame = 1