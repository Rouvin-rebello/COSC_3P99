import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def simulate_shoot_right(self, line):
        if line:
            yield line

