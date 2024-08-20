from hitbox import *

def clip(self, arg):
    if isinstance(arg, Ellipse):
        return self._clip_ellipse(Ellipse(arg))
    return self._clip_rect(Rect(arg))
