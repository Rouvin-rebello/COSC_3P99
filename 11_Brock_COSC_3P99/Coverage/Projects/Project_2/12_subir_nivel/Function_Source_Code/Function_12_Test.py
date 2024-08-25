import unittest
from Function_12_Source import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_subir_nivel_deve_aumentar_o_attr_nivel_do_pokemon(self):
        nivel_antes_de_subir = self.pokemon.nivel
        self.pokemon.subir_nivel()
        self.assertEqual(nivel_antes_de_subir + 2, self.pokemon.nivel)

    def test_reconfigurar_status_deve_reconfigurar_todos_os_attr_de_acordo_com_o_novo_nivel(self):
        vida_antes_pokemon = self.pokemon.vida
        ataque_base_antes_pokemon = self.pokemon.ataque_base
        self.pokemon.subir_nivel()
        self.assertNotEqual(self.pokemon.vida, vida_antes_pokemon)
        self.assertNotEqual(self.pokemon.ataque_base, ataque_base_antes_pokemon)

if __name__ == '__main__':
    unittest.main()

