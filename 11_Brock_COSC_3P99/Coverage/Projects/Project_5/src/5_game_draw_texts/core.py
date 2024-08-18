import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def draw_texts(self):
    self.draw_number(self.score, 0, self.maze.shape[0] * TILE_SIZE)

    for i in range(0, self.player.lives):
        self.screen.blit(
            self.img_life, (
                (self.maze.shape[1] // 2 - 1) * TILE_SIZE + i * 10,
                self.maze.shape[0] * TILE_SIZE))