from mixins import *
def update(self) -> None:
    if self.tick_hover > 0.7:
        self.is_hover = True