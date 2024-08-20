import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def event_loop(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            self.quit_game()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.is_run = False
                self.start_game(restart=True)
                if self.sounds_active:
                    self.channel_background.stop()