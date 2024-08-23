from hitbox import *
from mixins import *

# def clamp_ip(self, arg):
#         try:
#             self.__class__(arg)
#         except Exception:
#             raise TypeError("Argument must be hitbox style object")

#         if isinstance(arg, Ellipse):
#             return self._clamp_ip_ellipse(Ellipse(arg))
#         return self._clamp_ip_rect(Rect(arg))

# def clip(self, arg):
#         try:
#             self.__class__(arg)
#         except Exception:
#             raise TypeError("Argument must be hitbox style object")

#         if isinstance(arg, Ellipse):
#             return self._clip_ellipse(Ellipse(arg))
#         return self._clip_rect(Rect(arg))

# def union_ip(self, arg):
#         try:
#             self.__class__(arg)
#         except Exception:
#             raise TypeError("Argument must be hitbox style object")

#         if isinstance(arg, Ellipse):
#             return self._union_ip_ellipse(Ellipse(arg))
#         return self._union_ip_rect(arg)

# def fit(self, arg):
#         try:
#             self.__class__(arg)
#         except Exception:
#             raise TypeError("Argument must be hitbox style object")

#         if isinstance(arg, Ellipse):
#             return self._fit_ellipse(Ellipse(arg))
#         return self._fit_rect(Rect(arg))

# def colliderect(self, arg):
#         try:
#             self.__class__(arg)
#         except Exception:
#             raise TypeError("Argument must be hitbox style object")

#         if 0 in [self.w, self.h, arg.w, arg.h]:
#             return False

#         if isinstance(arg, Ellipse):
#             return self._colliderect_ellipse(Ellipse(arg))
#         return self._colliderect_rect(Rect(arg))

# def fy(self, x):
#         cx, cy = self.center
#         d = 1 - (x - cx) ** 2 / self.a ** 2

#         if d >= 0:
#             d = sqrt(d)
#             return (cy - self.b * d, cy + self.b * d)
#         return ()

def update(self) -> None:
        """Updates boost
        """
        # If boost was activated
        if self.is_active:
            # Count life time
            self.life -= self.config['ns'].dt / 30

            if self.life <= 0:
                # Deactivate and kill the boost if there is no time left
                self.deactivate()
                self.kill()
                return

            # Vertical positioning of boost, taking into account the number in the boost queue
            self.rect_small.top = self.screen_rect.top + 2 * self.number_in_queue + 18 * (self.number_in_queue - 1)

            # Generating text with the remaining lifetime
            if ceil(self.life) <= 3:
                # Rendering text using *COLOR_SHORT*, if there is little time left
                self.img_life = self.font.render(f"{ceil(self.life)}S", True, self.COLOR_SHORT)
                self.rect_life = self.img_life.get_rect()
                self.rect_life.top = self.screen_rect.top + 2 * self.number_in_queue + 18 * (self.number_in_queue - 1)
                self.rect_life.left = self.screen_rect.left + 24
            else:
                # Rendering text using *COLOR_LONG*, if there is a lot of time left
                self.img_life = self.font.render(f"{ceil(self.life)}S", True, self.COLOR_LONG)
                self.rect_life = self.img_life.get_rect()
                self.rect_life.top = self.screen_rect.top + 2 * self.number_in_queue + 18 * (self.number_in_queue - 1)
                self.rect_life.left = self.screen_rect.left + 24
        else:
            # Continue movement of boost if it has not activated yet
            self.rect_idle.x -= self.config['ns'].speed * self.config['ns'].dt

        # Kill boost if it has left the screen
        if self.rect_idle.right < 0:
            self.kill()
