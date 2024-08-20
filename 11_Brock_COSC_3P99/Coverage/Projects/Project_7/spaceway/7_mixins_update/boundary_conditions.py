from mixins import *
def update(self) -> None:
    point = pygame.mouse.get_pos()

    if self.rect.collidepoint(point):
        # If mouse hovered on button, continue countdown
        self.tick_hover += self.config['ns'].dt / 30
    else:
        # Otherwise, reset the tick to stop the countdown
        self.tick_hover = 0
        self.is_hover = False