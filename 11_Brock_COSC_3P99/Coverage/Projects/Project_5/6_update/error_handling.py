import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def update(self):
    if self.status in {Status.WIN, Status.GAMEOVER}:
        self.quit_game()