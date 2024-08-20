from hitbox import *
def fit(self, arg):
        if isinstance(arg, Ellipse):
            return self._fit_ellipse(Ellipse(arg))
        return self._fit_rect(Rect(arg))
