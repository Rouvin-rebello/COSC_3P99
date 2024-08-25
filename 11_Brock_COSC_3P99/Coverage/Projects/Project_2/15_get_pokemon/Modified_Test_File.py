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
from core_functionality import PokemonFactory
from pokemon import Onix, Charmander, Magicarpa, Pikachu, Pokemon

class TestPokemonFactory(unittest.TestCase):
    def test_get_pokemon_aleatorio(self):
        pokemon = PokemonFactory.get_pokemon()
        self.assertIsInstance(pokemon, Pokemon)

    def test_get_pokemon_nome_onix(self):
        pokemon = PokemonFactory.get_pokemon(nome='onix')
        self.assertIsInstance(pokemon, Onix)

    def test_get_pokemon_nome_charmander(self):
        pokemon = PokemonFactory.get_pokemon(nome='charmander')
        self.assertIsInstance(pokemon, Charmander)

    def test_get_pokemon_nome_magicarpa(self):
        pokemon = PokemonFactory.get_pokemon(nome='magicarpa')
        self.assertIsInstance(pokemon, Magicarpa)

    def test_get_pokemon_nome_pikachu(self):
        pokemon = PokemonFactory.get_pokemon(nome='pikachu')
        self.assertIsInstance(pokemon, Pikachu)

    def test_get_pokemon_nivel_especifico(self):
        nivel = 10
        pokemon = PokemonFactory.get_pokemon(nivel=nivel)
        self.assertEqual(pokemon.nivel, nivel)

    def test_get_pokemon_nome_e_nivel_especifico(self):
        nome = 'charmander'
        nivel = 15
        pokemon = PokemonFactory.get_pokemon(nome=nome, nivel=nivel)
        self.assertIsInstance(pokemon, Charmander)
        self.assertEqual(pokemon.nivel, nivel)


if __name__ == '__main__':
    unittest.main()
