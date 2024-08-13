from pybubble_shooter import *
def simulate_shoot_right(self, line):
        """Yield lines on which a bullet shot to the right first will move.
           Args:
             start (Point): at where a bullet is shot
             end (Point): where a bullet will collid first with the screen right wall.
        """
        if line:
            yield line

