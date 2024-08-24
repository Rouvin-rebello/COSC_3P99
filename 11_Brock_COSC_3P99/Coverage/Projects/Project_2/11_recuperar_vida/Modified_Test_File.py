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
from core_functionality import Pokemon
from boundary_conditions import test_boundary_conditions
from output_consistency import test_output_consistency

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_recuperar_vida_esta_restaurando_a_vida_corretamente_de_acordo_com_o_seu_level(self):
        vida_completa_pokemon = self.pokemon.vida
        self.pokemon.vida -= 20
        self.pokemon.recuperar_vida()
        self.assertEqual(vida_completa_pokemon, self.pokemon.vida)

    def test_boundary_conditions(self):
        test_boundary_conditions()

    def test_output_consistency(self):
        test_output_consistency()

if __name__ == '__main__':
    unittest.main()
