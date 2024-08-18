import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import *

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