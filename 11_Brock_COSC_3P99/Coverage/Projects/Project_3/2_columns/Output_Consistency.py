# Output_Consistency.py

class Board(object):
    @property
    def columns(self):
        return list(map(list, zip(*self.rows)))
