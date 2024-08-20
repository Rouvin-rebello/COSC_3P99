from hitbox import *

def union_ip(self, arg):
        if isinstance(arg, Ellipse):
            return self._union_ip_ellipse(Ellipse(arg))
        return self._union_ip_rect(arg)
