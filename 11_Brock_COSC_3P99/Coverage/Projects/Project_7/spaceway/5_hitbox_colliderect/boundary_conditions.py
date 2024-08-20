from hitbox import *

def colliderect(self, arg):
    if 0 in [self.w, self.h, arg.w, arg.h]:
        return False