import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacman import *

def move(self, game):
        poss_x, poss_y = self.x + self.vel_x, self.y + self.vel_y
        if not game.check_if_player_hit_wall(poss_x, poss_y):
            self.x += self.vel_x
            self.y += self.vel_y

            game.check_if_hit_something()
            game.check_collision_with_ghosts()
            # todo: check collision with fruit
        else:
            self.vel_y, self.vel_x = 0, 0