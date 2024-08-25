try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise

import unittest
import logging
from io import StringIO
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Pokemon(nivel=10)
        # Set up the logger to capture output for the test
        self.log_stream = StringIO()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(self.log_stream)
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def tearDown(self) -> None:
        # Remove handlers after test to avoid duplicate logs
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

    def test_apresentar_pokemon(self):
        """
        Teste para verificar a saída do método apresentar_pokemon.
        """
        expected_output = (
            f'pokemon: {self.pokemon.__class__.__name__}\n'
            f'Level: {self.pokemon.nivel}\n'
            f'Vida: {self.pokemon.vida} de pontos.\n'
            f'Dano base: {self.pokemon.ataque_base}\n'
        )

        # Call the method to log the output
        self.pokemon.apresentar_pokemon()

        # Get the log output
        log_output = self.log_stream.getvalue()

        # Ensure the log output matches the expected output
        self.assertEqual(log_output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
