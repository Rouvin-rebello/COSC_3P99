from hitbox import *

def union_ip(self, arg):
        try:
            self.__class__(arg)
        except Exception:
            raise TypeError("Argument must be hitbox style object")