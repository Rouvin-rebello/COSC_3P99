import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def decide_positions(self, start, end, compare_position,x,y):
    if compare_position(end, x, y):
        pass_pt = Point(x, y)
        yield pass_pt
        yield from self.decide_positions(pass_pt, end, compare_position)
    else:
        yield self.shooter.dest.center