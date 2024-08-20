import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def simulate_shoot_right(self, is_stop, line, start, end):
        if not is_stop:
            angle = 90 - self.launcher_angle
            for line in self._simulate_bounce_course(angle, end, is_stop, True):
                yield line

