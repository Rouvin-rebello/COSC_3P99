from hitbox import *
def colliderect(self, arg):
    if isinstance(arg, Ellipse):
        return self._colliderect_ellipse(Ellipse(arg))
    return self._colliderect_rect(Rect(arg))