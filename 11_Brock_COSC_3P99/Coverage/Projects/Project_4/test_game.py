import sys
import os
from typing import Any
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from snake.direction import Direction
from game import *
# from snake.types import Position
# from snake.ui.protocol import UiProtocol
from unittest.mock import Mock, call, DEFAULT
from typing import Callable, Any, List, Union, Generator
import pytest
import signal


class BaseTestCase:
    ui: Any
    egg_creator: Any

    def get_drawn_snakes(self) -> List[List[Position]]:
        call_args = [call.kwargs for call in self.ui.draw.call_args_list]
        return [args["snake"] for args in call_args]


class TestGame(BaseTestCase):
    snake: List[Position] = [(7, 5), (6, 5), (5, 5)]
    size: int = 20

    def setup_method(self) -> None:
        self.ui = Mock()
        self.ui.direction = mock_direction()
        self.egg_creator = Mock()
        self.egg_creator.create.return_value = (0, 0)

    def test_snake_moves_right(self) -> None:
        game = Game(iterations=2,
                    snake=self.snake,
                    size=self.size,
                    ui=self.ui,
                    egg_creator=self.egg_creator)
        game.run()
        assert self.get_drawn_snakes() == [
            [(7, 5), (6, 5), (5, 5)],
            [(8, 5), (7, 5), (6, 5)]
        ]

    def test_snake_size_zero_fails(self) -> None:
        with pytest.raises(Exception):
            # don't really care how it fails ...
            game = Game(iterations=2, snake=[], size=20,
                        ui=self.ui, egg_creator=self.egg_creator)
            game.run()

    def test_snake_changes_direction(self) -> None:
        self.ui.direction = mock_direction(
            [Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT]
        )
        game = Game(iterations=5, snake=self.snake,
                    size=self.size,
                    ui=self.ui,
                    egg_creator=self.egg_creator)
        game.run()
        assert self.get_drawn_snakes() == [
            [(7, 5), (6, 5), (5, 5)],
            [(7, 4), (7, 5), (6, 5)],
            [(6, 4), (7, 4), (7, 5)],
            [(6, 5), (6, 4), (7, 4)],
            [(7, 5), (6, 5), (6, 4)]
        ]

    def test_snake_keeps_direction(self) -> None:
        self.ui.direction = mock_direction(Direction.UP)
        game = Game(iterations=3, snake=self.snake,
                    size=self.size,
                    ui=self.ui,
                    egg_creator=self.egg_creator)
        game.run()
        assert self.get_drawn_snakes() == [
            [(7, 5), (6, 5), (5, 5)],
            [(7, 4), (7, 5), (6, 5)],
            [(7, 3), (7, 4), (7, 5)]
        ]

    def test_cannot_go_back(self) -> None:
        self.ui.direction = mock_direction([Direction.RIGHT, Direction.LEFT])
        self.egg_creator.create.return_value = (3, 3)
        game = Game(
            snake=[(1, 0), (0, 0)],
            iterations=3,
            size=4,
            ui=self.ui,
            egg_creator=self.egg_creator
        )
        game.run()
        assert self.get_drawn_snakes() == [
            [(1, 0), (0, 0)],
            [(2, 0), (1, 0)],
            [(3, 0), (2, 0)]
        ]

    def test_loop_over(self) -> None:
        snake = [(3, 0), (2, 0)]
        self.egg_creator.create.return_value = [3, 3]
        self.ui.direction = mock_direction(Direction.RIGHT)
        game = Game(
            snake=[(3, 0), (2, 0)],
            iterations=2,
            size=4,
            ui=self.ui,
            egg_creator=self.egg_creator
        )
        game.run()
        assert [(0, 0), (3, 0)] in self.get_drawn_snakes()

    def test_infinite_iterations(self) -> None:
        try:
            with Timeout():
                Game(iterations=None, snake=self.snake,
                     size=self.size,
                     ui=self.ui,
                     egg_creator=self.egg_creator).run()
        except TimeoutError:
            pass
        else:
            raise AssertionError('Expected the thing to timeout!')

    def test_snake_eats_itself(self) -> None:
        self.ui.direction = mock_direction(Direction.RIGHT)
        game = Game(size=20, ui=self.ui, snake=[
                    (0, 1), (0, 0), (1, 0), (1, 1), (1, 2)])
        with Timeout():
            assert game.run() is False


class TestEggInteraction(BaseTestCase):
    def get_drawn_eggs(self) -> List[Position]:
        call_args = [call.kwargs for call in self.ui.draw.call_args_list]
        return [args["egg"] for args in call_args]

    def setup_method(self) -> None:
        self.ui = Mock()
        self.ui.direction = mock_direction()
        self.default_params = {
            "snake": [(1, 0), (0, 0)], "size": 20, "ui": self.ui
        }

    def test_place_egg(self) -> None:
        egg_creator = Mock()
        egg_creator.create.side_effect = [(10, 10), (15, 15)]
        game = Game(iterations=2, egg_creator=egg_creator,
                    ui=self.ui, snake=[(1, 0), (0, 0)])
        game.run()
        assert self.get_drawn_eggs() == [
            (10, 10),  # draw once
            (10, 10)  # it hasn't moved
        ]

    def test_eat_egg_place_new_egg(self) -> None:
        egg_creator = Mock()
        egg_creator.create.side_effect = [(2, 0), (10, 10)]
        game = Game(iterations=3, egg_creator=egg_creator,
                    ui=self.ui, snake=[(1, 0), (0, 0)])
        game.run()
        assert self.get_drawn_eggs() == [
            (2, 0),
            (10, 10),
            (10, 10)
        ]

    def test_eat_egg_snake_grows(self) -> None:
        egg_creator = Mock()
        egg_creator.create.side_effect = [(2, 0), (10, 10)]
        game = Game(iterations=2, egg_creator=egg_creator,
                    ui=self.ui, snake=[(1, 0), (0, 0)])
        game.run()
        assert self.get_drawn_snakes() == [
            [(1, 0), (0, 0)],
            [(2, 0), (1, 0), (0, 0)]
        ]

    def test_egg_cannot_be_placed_on_snake(self) -> None:
        egg_creator = Mock()
        egg_creator.create.side_effect = [(0, 0), (15, 15)]
        game = Game(iterations=1, egg_creator=egg_creator,
                    ui=self.ui, snake=[(1, 0), (0, 0)])
        game.run()
        assert self.get_drawn_eggs() == [
            (15, 15)
        ]

    def test_eat_last_egg(self) -> None:
        egg_creator = Mock()
        egg_creator.create.return_value = (1, 1)
        self.ui.direction = mock_direction(Direction.RIGHT)
        game = Game(egg_creator=egg_creator,
                    ui=self.ui,
                    snake=[(0, 1), (0, 0), (1, 0)],
                    size=2)

        with Timeout():
            result = game.run()
            assert result is True


class TestRandomEggCreator():
    def test_create_in_bounds(self) -> None:
        creator = RandomEggCreator(23)
        for _ in range(1000):
            egg = creator.create()
            assert egg[0] in list(range(23))
            assert egg[1] in list(range(23))

    def test_create_is_random(self) -> None:
        expected_positions = [
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 1)
        ]
        creator = RandomEggCreator(2)
        with Timeout():
            while len(expected_positions) > 0:
                egg = creator.create()
                if egg in expected_positions:
                    expected_positions.remove(egg)


def mock_direction(directions: Union[Direction, List[Direction]] = None) -> Callable[[], Direction]:
    if directions is None:
        return Mock(return_value=None)
    elif not isinstance(directions, list):
        directions = [directions]

    def func() -> Generator[Direction, None, None]:
        for direction in directions:  # type: ignore
            yield direction
        while True:
            yield DEFAULT

    generator = func()

    def effect(*args: Any, **kwargs: Any) -> Direction:
        return next(generator)

    return Mock(
        side_effect=effect,
        return_value=None
    )


class Timeout:
    def __init__(self, seconds: float = .1, error_message: str = 'Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum: Any, frame: Any) -> None:
        raise TimeoutError(self.error_message)

    def __enter__(self) -> None:
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        signal.alarm(0)

class TestSnake():

    board = Board(4, 4)

    def test_create_default_positions(self) -> None:
        snake = Snake(self.board)
        assert snake.positions == [(1, 0), (0, 0)]
        assert snake.direction == Direction.RIGHT

    def test_create_given_positions(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (1, 0)])
        assert snake.positions == [(0, 0), (1, 0)]

    def test_create_must_have_two_or_more_positions(self) -> None:
        with pytest.raises(Exception) as e:
            snake = Snake(self.board, positions=[])
        assert str(e.value) == "snake should have a length of at least 2"

        with pytest.raises(Exception) as e:
            snake = Snake(self.board, positions=[(0, 0)])
        assert str(e.value) == "snake should have a length of at least 2"

    def test_compute_direction(self) -> None:
        # TODO: test through the public API ; direction should not be part of the public api
        assert Snake(self.board, positions=[(1, 0), (0, 0)]).direction \
            == Direction.RIGHT
        assert Snake(self.board, positions=[(0, 0), (1, 0)]).direction \
            == Direction.LEFT
        assert Snake(self.board, positions=[(0, 0), (0, 1)]).direction \
            == Direction.UP
        assert Snake(self.board, positions=[(0, 1), (0, 0)]).direction \
            == Direction.DOWN

        assert Snake(self.board, positions=[(3, 0), (0, 0)]).direction \
            == Direction.LEFT
        assert Snake(self.board, positions=[(0, 0), (3, 0)]).direction \
            == Direction.RIGHT
        assert Snake(self.board, positions=[(0, 3), (0, 0)]).direction \
            == Direction.UP
        assert Snake(self.board, positions=[(0, 0), (0, 3)]).direction \
            == Direction.DOWN

    def test_move_right(self) -> None:
        snake = Snake(self.board, positions=[(1, 0), (0, 0)])
        snake.move(False)
        assert snake.positions == [(2, 0), (1, 0)]

    def test_move_left(self) -> None:
        snake = Snake(self.board, positions=[(1, 0), (2, 0)])
        snake.move()
        assert snake.positions == [(0, 0), (1, 0)]

    def test_move_up(self) -> None:
        snake = Snake(self.board, positions=[(0, 1), (0, 2)])
        snake.move()
        assert snake.positions == [(0, 0), (0, 1)]

    def test_move_down(self) -> None:
        snake = Snake(self.board, positions=[(0, 1), (0, 0)])
        snake.move()
        assert snake.positions == [(0, 2), (0, 1)]

    def test_move_keep_tail(self) -> None:
        snake = Snake(self.board, positions=[(1, 0), (0, 0)])
        snake.move(True)
        assert snake.positions == [(2, 0), (1, 0), (0, 0)]

    def test_bite_itself(self) -> None:
        snake = Snake(self.board, positions=[
                      (0, 1), (0, 0), (1, 0), (1, 1), (1, 2)])
        snake.direction = Direction.RIGHT
        with pytest.raises(Snake.BitesItselfError):
            snake.move()

    def test_fills_board(self) -> None:
        board = Board(2, 3)
        small_snake = Snake(board, positions=[(0, 0), (1, 0)])
        big_snake = Snake(board, positions=[
            (0, 2), (0, 1), (0, 0), (1, 0), (1, 1), (1, 2)])
        assert small_snake.fills_board() is False
        assert big_snake.fills_board() is True

    def test_will_eat_egg(self) -> None:
        snake = Snake(self.board, positions=[(1, 0), (0, 0)])
        assert snake.will_eat_egg((2, 0)) is True
        assert snake.will_eat_egg((1, 1)) is False

    def test_iter(self) -> None:
        snake = Snake(self.board, positions=[(0, 1), (0, 0)])
        assert [pos for pos in snake] == [(0, 1), (0, 0)]


class TestLoopOver():
    board = Board(width=4, height=6)

    def test_left(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (1, 0)])
        snake.move()
        assert snake.positions == [(3, 0), (0, 0)]

    def test_right(self) -> None:
        snake = Snake(self.board, positions=[(3, 0), (2, 0)])
        snake.move()
        assert snake.positions == [(0, 0), (3, 0)]

    def test_up(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (0, 1)])
        snake.move()
        assert snake.positions == [(0, 5), (0, 0)]

    def test_down(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (0, 1)])
        snake.move()
        assert snake.positions == [(0, 5), (0, 0)]


class TestChangeDirection():
    board = Board(width=4, height=6)

    def test_left(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (1, 0)])
        snake.direction = Direction.RIGHT
        snake.move()
        assert snake.positions == [(3, 0), (0, 0)]

    def test_right(self) -> None:
        snake = Snake(self.board, positions=[(3, 0), (2, 0)])
        snake.direction = Direction.LEFT
        snake.move()
        assert snake.positions == [(0, 0), (3, 0)]

    def test_up(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (0, 1)])
        snake.direction = Direction.DOWN
        snake.move()
        assert snake.positions == [(0, 5), (0, 0)]

    def test_down(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (0, 1)])
        snake.direction = Direction.UP
        snake.move()
        assert snake.positions == [(0, 5), (0, 0)]

    def test_none_no_change(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (1, 0)])
        snake.direction = None  # type: ignore
        snake.move()
        assert snake.positions == [(3, 0), (0, 0)]

    def test_default_no_change(self) -> None:
        snake = Snake(self.board, positions=[(0, 0), (1, 0)])
        snake.direction = Direction.DEFAULT
        snake.move()
        assert snake.positions == [(3, 0), (0, 0)]

if __name__ == '__main__':
    pytest.main()
