import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def simulate_shoot_left(self, start, end):
        is_stop, line = self._simulate_course(start, end)