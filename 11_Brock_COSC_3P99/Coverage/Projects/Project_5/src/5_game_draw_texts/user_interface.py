import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def draw_texts(self):
    if self.game_mode == 3:
        self.screen.blit(self.img_game_over, self.set_text_center(self.img_game_over))
    elif self.game_mode in [GameMode.ready, GameMode.wait_to_start]:
        self.screen.blit(self.img_ready, self.set_text_center(self.img_ready))