from pybubble_shooter import *

def calculate_sides(self):
    half = BUBBLE_SIZE // 2  # Boundary condition if BUBBLE_SIZE is odd

def calculate_center(self):
    if self.row % 2 == 0:  # Edge case handling for even/odd row parity
        start = X_START_POS
    else:
        start = X_START_POS + BUBBLE_SIZE // 2

