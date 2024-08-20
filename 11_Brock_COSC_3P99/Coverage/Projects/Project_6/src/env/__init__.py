from gym.envs.registration import register # type: ignore

register(
    id='pacman-v0',
    entry_point='src.env.pacman_env:PacmanEnv',
)
