import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *

def calculate_sides(self):
    half = BUBBLE_SIZE // 2
    left_top = Point(self.center.x - half, self.center.y - half)
    right_bottom = Point(self.center.x + half, self.center.y + half)
    right_top = Point(self.center.x + half, self.center.y - half)
    left_bottom = Point(self.center.x - half, self.center.y + half)

    self.left = Line(left_top, left_bottom)
    self.right = Line(right_top, right_bottom)
    self.top = Line(left_top, right_top)
    self.bottom = Line(left_bottom, right_bottom)

def calculate_center(self):
    start = X_START_POS
    x = start + BUBBLE_SIZE * self.col
    y = Y_START_POS + BUBBLE_SIZE * self.row
    self.center = Point(x, y)
