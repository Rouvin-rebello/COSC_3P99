import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacman import *

def draw(self, screen, game_mode):
    if self.vel_x > 0:
        self.current_anim = self.anim_r
    elif self.vel_x < 0:
        self.current_anim = self.anim_l
    elif self.vel_y > 0:
        self.current_anim = self.anim_d
    elif self.vel_y < 0:
        self.current_anim = self.anim_u