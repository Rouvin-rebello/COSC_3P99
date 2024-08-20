import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pybubble_shooter import *
def update(self):
    if 0 < self.launcher_angle <= self.limit_angle:
        y = WINDOW.height - self.calculate_height(self.launcher_angle, WINDOW.half_width)
        pt = Point(WINDOW.width, y)
        self.course = [line for line in self.simulate_shoot_right(self.launcher, pt)]
    elif self.launcher_angle >= 180 - self.limit_angle:
        y = WINDOW.height - self.calculate_height(180 - self.launcher_angle, WINDOW.half_width)
        pt = Point(0, y)
        self.course = [line for line in self.simulate_shoot_left(self.launcher, pt)]
    else:
        if self.limit_angle < self.launcher_angle <= 90:
            x = WINDOW.half_width + self.calculate_height(90 - self.launcher_angle, WINDOW.height)
        elif 90 < self.launcher_angle < 180 - self.limit_angle:
            x = WINDOW.half_width - self.calculate_height(self.launcher_angle - 90, WINDOW.height)
        self.course = [line for line in self.simulate_shoot_top(self.launcher, Point(x, 0))]
