from hitbox import *

def clamp_ip(self, arg):
    if isinstance(arg, Ellipse):
        return self._clamp_ip_ellipse(Ellipse(arg))
    return self._clamp_ip_rect(Rect(arg))