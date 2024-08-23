from pacman import *
from game import *

def move(self, game):
    self.nearest_row = int(((self.y + TILE_SIZE / 2) / TILE_SIZE))
    self.nearest_col = int(((self.x + TILE_SIZE / 2) / TILE_SIZE))
    poss_x, poss_y = self.x + self.vel_x, self.y + self.vel_y

    if not game.check_if_player_hit_wall(poss_x, poss_y):
        self.x += self.vel_x
        self.y += self.vel_y

        game.check_if_hit_something()
        game.check_collision_with_ghosts()
        # todo: check collision with fruit
    else:
        self.vel_y, self.vel_x = 0, 0

def draw(self, screen, game_mode):

    if game_mode == GameMode.game_over:
        return False

    # set the current frame array to match the direction pacman is facing
    if self.vel_x > 0:
        self.current_anim = self.anim_r
    elif self.vel_x < 0:
        self.current_anim = self.anim_l
    elif self.vel_y > 0:
        self.current_anim = self.anim_d
    elif self.vel_y < 0:
        self.current_anim = self.anim_u

    screen.blit(self.current_anim[self.anim_frame],
                (self.x, self.y))

    if game_mode in [GameMode.normal, GameMode.change_ghosts, GameMode.wait_after_eating_ghost]:
        if not self.vel_x == 0 or not self.vel_y == 0:
            self.anim_frame += 1

        if self.anim_frame == 9:
            self.anim_frame = 1

def start_game(self, restart=False):
        if restart:
            self.maze.reinit_map()
            self.player.lives = 3

        self.set_mode(0)
        self.init_game()
        self.init_players_in_map()
        self.player.set_vel_to_zero()
        self.game_loop()

def event_loop(self):
        if self.game_mode in MOVE_MODES:
            if self.ai_agent is None:
                action = Game.check_keyboard_inputs()
            else:
                action = self.ai_agent.act(
                    player_pos=self.player.get_position(),
                    player_pixel_pos=self.player.get_pixel_pos(),
                    matrix=self.maze.get_state_matrix(),
                    ghost_positions=[(ghost.nearest_col, ghost.nearest_row) \
                                     for ghost in self.ghosts],
                    screen=pg.surfarray.pixels3d(self.prev_screen),
                    player_action=self.player.current_action)
                action = int(action)

            if action is not None:
                self.player.change_player_vel(action, self)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_run = False
                    self.start_game(restart=True)
                    if self.sounds_active:
                        self.channel_background.stop()

def draw_texts(self):
        self.draw_number(self.score, 0, self.maze.shape[0] * TILE_SIZE)

        for i in range(0, self.player.lives):
            self.screen.blit(
                self.img_life, (
                    (self.maze.shape[1] // 2 - 1) * TILE_SIZE + i * 10,
                    self.maze.shape[0] * TILE_SIZE))
            
def set_mode(self, mode: Union[int, GameMode]):
        self.game_mode = GameMode(mode) if type(mode) is int else mode
        if self.game_mode in MODES_TO_ZERO:
            self.mode_timer = 0
        if self.sounds_active:
            self.set_proper_bkg_music()

def check_ghost_state(self, path_finder: PathFinder, player: Pacman):
        if self.nearest_row == self.respawn_y \
            and self.nearest_col == self.respawn_x \
                and self.state == GhostState.spectacles:
            self.state = GhostState.normal
            self.speed = 2
            self.find_path(path_finder, player)