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
from core_functionality import Charmander, Magicarpa, Onix, Pikachu, Pokemon, PokemonAgua, PokemonEletrico, PokemonFogo, PokemonPedra
from ataque import AtaqueNormal,AtaqueComForca
from pokemon import Pokemon


class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_pokemon_attr_nivel_tem_o_valor_correto(self):
        self.assertEqual(self.pokemon.nivel, self.nivel_pokemon)

    def test_pokemon_attr_vida_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.vida, 10 * self.nivel_pokemon)

    def test_pokemon_attr_ataque_base_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.ataque_base, 4 * self.nivel_pokemon)

class TestCharmander(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Charmander()

    def test_pokemon_pode_atacar(self):
        self.assertTrue(hasattr(self.pokemon, 'atacar'))

class TestMagicarpa(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Magicarpa()

    def test_pokemon_pode_atacar(self):
        self.assertTrue(hasattr(self.pokemon, 'atacar'))

class TestOnix(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Onix()

    def test_pokemon_pode_atacar(self):
        self.assertTrue(hasattr(self.pokemon, 'atacar'))

class TestPikachu(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon = Pikachu()

    def test_pokemon_pode_atacar(self):
        self.assertTrue(hasattr(self.pokemon, 'atacar'))

if __name__ == '__main__':
    unittest.main()
