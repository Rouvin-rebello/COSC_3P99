import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

def set_mode(self, mode: Union[int, GameMode]):
    if self.game_mode in MODES_TO_ZERO:
        self.mode_timer = 0
    if self.sounds_active:
        self.set_proper_bkg_music()