from mixins import *
def update(self) -> None:
    self.img = self.imgs[self.state]
    self.img_hint = self.imgs_hint[self.state]
    self.config['user'][self.config_index] = self.state
