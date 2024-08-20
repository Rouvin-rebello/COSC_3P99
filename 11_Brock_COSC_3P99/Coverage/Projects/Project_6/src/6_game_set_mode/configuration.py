import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def set_mode(self, mode: Union[int, GameMode]):
    self.game_mode = GameMode(mode) if type(mode) is int else mode
