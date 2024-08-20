import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def update(self):
    if self.dest:
        for line in self.course:
            pygame.draw.line(self.screen, Colors.DARK_GREEN.color_code, line.start, line.end, 2)
