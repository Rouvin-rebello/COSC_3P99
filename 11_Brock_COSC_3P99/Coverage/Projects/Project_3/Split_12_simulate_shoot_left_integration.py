from pybubble_shooter import *
# def simulate_shoot_left(self, line, is_stop, start, end):
#         """Yield lines on which a bullet shot to the left first will move.
#            Args:
#              start (Point): at where a bullet is shot
#              end (Point): where a bullet will collid first with the screen right wall.
#         """
#         if not is_stop:
#             angle = self.launcher_angle - 90
#             for line in self._simulate_bounce_course(angle, end, is_stop, False):
#                 yield line
def _trace(self, start, end):
        """Follow a simulation line from bottom to top, and yield
           Cell that intersects the simulation line.
           Args:
             start (Point): one end of a simulation line
             end (Point): the another end of a simulation line
        """
        target = None
        step = 1 if start.x >= end.x else -1
        for cells in self.cells[::-1]:
            empty = None
            for cell in cells[::step]:
                if self.is_crossing(start, end, cell):
                    if not cell.bubble and not empty:
                        empty = cell
                    if cell.bubble:
                        target = cell
                        break
            if not target and empty:
                yield empty
            elif target:
                yield target
                break