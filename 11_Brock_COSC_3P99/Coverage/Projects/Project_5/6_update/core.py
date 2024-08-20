import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def update(self):
    if self.game == Status.PLAY:
        self.draw_setting()

    if self.status == Status.READY:
        if not (count := self.count_bubbles()):
            self.status = Status.WIN
        else:
            if self.bullet.status == Status.STAY:
                if self.is_decrease and count <= 10:
                    self.change_bubbles()
                    self.is_decrease = False
                if self.is_increase:
                    self.increase_bubbles(4)
                    self.is_increase = False

    if self.status == Status.CHARGE:
        self.charge()