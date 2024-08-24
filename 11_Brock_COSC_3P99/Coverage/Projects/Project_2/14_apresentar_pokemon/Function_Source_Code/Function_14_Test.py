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
from io import StringIO
import sys

from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Pokemon(nivel=10)

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

        # Redirect stdout to capture print statements
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            self.pokemon.apresentar_pokemon()
            output = sys.stdout.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            # Reset stdout to its original state
            sys.stdout = original_stdout
