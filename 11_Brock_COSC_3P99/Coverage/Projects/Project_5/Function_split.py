from pybubble_shooter import *

def update(self):
        if self.game == Status.PLAY:
            self.draw_setting()

            if self.status == Status.READY:
                if not (count := self.count_bubbles()):
                    self.status = Status.WIN
                else:
                    if self.bullet.status == Status.STAY:
                        if self.is_decrease and count <= 10:
                            self.change_bubbles()
                            self.is_decrease = False
                        if self.is_increase:
                            self.increase_bubbles(4)
                            self.is_increase = False

                if any(cell.bubble for cell in self.cells[-1]):
                    self.status = Status.GAMEOVER

            if self.status in {Status.WIN, Status.GAMEOVER}:
                self.quit_game()

            if 0 < self.launcher_angle <= self.limit_angle:
                y = WINDOW.height - self.calculate_height(self.launcher_angle, WINDOW.half_width)
                pt = Point(WINDOW.width, y)
                self.course = [line for line in self.simulate_shoot_right(self.launcher, pt)]
            elif self.launcher_angle >= 180 - self.limit_angle:
                y = WINDOW.height - self.calculate_height(180 - self.launcher_angle, WINDOW.half_width)
                pt = Point(0, y)
                self.course = [line for line in self.simulate_shoot_left(self.launcher, pt)]
            else:
                if self.limit_angle < self.launcher_angle <= 90:
                    x = WINDOW.half_width + self.calculate_height(90 - self.launcher_angle, WINDOW.height)
                elif 90 < self.launcher_angle < 180 - self.limit_angle:
                    x = WINDOW.half_width - self.calculate_height(self.launcher_angle - 90, WINDOW.height)
                self.course = [line for line in self.simulate_shoot_top(self.launcher, Point(x, 0))]

            if self.dest:
                for line in self.course:
                    pygame.draw.line(self.screen, Colors.DARK_GREEN.color_code, line.start, line.end, 2)

            if self.status == Status.CHARGE:
                self.charge()
                self.status = Status.READY

def change_bubbles(self):
        if self.colors_count > 1:
            self.colors_count -= 1
        self.bubbles = random.sample(BUBBLES, self.colors_count)
        self.next_bullet = None
        self.charge()

        if len(self.bubbles) <= 2:
            self.delete_bubbles()
            self.create_bubbles(10)
        else:
            self.increase_bubbles(10)

def calculate_sides(self):
        half = BUBBLE_SIZE // 2
        left_top = Point(self.center.x - half, self.center.y - half)
        right_bottom = Point(self.center.x + half, self.center.y + half)
        right_top = Point(self.center.x + half, self.center.y - half)
        left_bottom = Point(self.center.x - half, self.center.y + half)

        self.left = Line(left_top, left_bottom)
        self.right = Line(right_top, right_bottom)
        self.top = Line(left_top, right_top)
        self.bottom = Line(left_bottom, right_bottom)

def calculate_center(self):
    if self.row % 2 == 0:
        start = X_START_POS
    else:
        start = X_START_POS + BUBBLE_SIZE // 2
    x = start + BUBBLE_SIZE * self.col
    y = Y_START_POS + BUBBLE_SIZE * self.row
    self.center = Point(x, y)

def move_bubble(self, move_to):
        if not move_to.bubble:
            self.bubble.rect.centerx = move_to.center.x
            self.bubble.rect.centery = move_to.center.y
            move_to.bubble = self.bubble
            self.bubble = None

def decide_positions(self, start, end, compare_position):
        dx = end.x - start.x
        dy = end.y - start.y
        distance = (dx**2 + dy ** 2) ** 0.5
        vx = dx * 10 / distance
        vy = dy * 10 / distance
        x = start.x + vx
        y = start.y + vy

        if compare_position(end, x, y):
            pass_pt = Point(x, y)
            yield pass_pt
            yield from self.decide_positions(pass_pt, end, compare_position)
        else:
            yield self.shooter.dest.center

def simulate_shoot_right(self, start, end):
        """Yield lines on which a bullet shot to the right first will move.
           Args:
             start (Point): at where a bullet is shot
             end (Point): where a bullet will collid first with the screen right wall.
        """
        is_stop, line = self._simulate_course(start, end)

        if line:
            yield line
        if not is_stop:
            angle = 90 - self.launcher_angle
            for line in self._simulate_bounce_course(angle, end, is_stop, True):
                yield line

def simulate_shoot_left(self, start, end):
    """Yield lines on which a bullet shot to the left first will move.
           Args:
             start (Point): at where a bullet is shot
             end (Point): where a bullet will collid first with the screen right wall.
    """
    is_stop, line = self._simulate_course(start, end)

    if line:
        yield line
    if not is_stop:
        angle = self.launcher_angle - 90
        for line in self._simulate_bounce_course(angle, end, is_stop, False):
            yield line
