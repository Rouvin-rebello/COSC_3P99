import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def update(self):
    if self.status == Status.READY:
        if not (count := self.count_bubbles()):  # No bubbles left
            self.status = Status.WIN
        elif any(cell.bubble for cell in self.cells[-1]):  # Bubbles reach bottom row
            self.status = Status.GAMEOVER