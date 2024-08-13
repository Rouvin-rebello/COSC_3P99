from pybubble_shooter import *

def decide_positions(self, start, end, compare_position):
    dx = end.x - start.x
    dy = end.y - start.y
    distance = (dx**2 + dy ** 2) ** 0.5
    vx = dx * 10 / distance
    vy = dy * 10 / distance
    x = start.x + vx
    y = start.y + vy