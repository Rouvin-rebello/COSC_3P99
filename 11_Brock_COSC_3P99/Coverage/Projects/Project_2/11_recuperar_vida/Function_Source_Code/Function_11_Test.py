import unittest
from Function_11_Source import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_recuperar_vida_esta_restaurando_a_vida_corretamente_de_acordo_com_o_seu_level(self):
        vida_completa_pokemon = self.pokemon.vida
        self.pokemon.vida -= 20
        self.pokemon.recuperar_vida()
        self.assertEqual(vida_completa_pokemon, self.pokemon.vida)

if __name__ == '__main__':
    unittest.main()

