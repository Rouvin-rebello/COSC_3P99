import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def simulate_shoot_left(self, start, end, is_stop):
        if not is_stop:
            angle = self.launcher_angle - 90
            for line in self._simulate_bounce_course(angle, end, is_stop, False):
                yield line