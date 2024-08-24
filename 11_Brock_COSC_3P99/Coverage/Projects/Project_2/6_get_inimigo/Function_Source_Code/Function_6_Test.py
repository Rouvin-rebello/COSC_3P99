import unittest
from Function_6_Source import Inimigo, InimigoFactory
from pokemon import Pokemon

class TestInimigoFactory(unittest.TestCase):
    def test_verificando_o_retorno_se_e_um_objeto_do_tipo_inimigo(self):
        self.assertIsInstance(InimigoFactory.get_inimigo(), Inimigo)

    def test_verificando_se_os_pokemons_adicionados_ao_objeto_inimigo_sao_realmente_objetos_do_tipo_pokemon(self):
        pokemons = [pokemon for pokemon in InimigoFactory.get_inimigo().lista_pokemons]
        for pokemon in pokemons:
            with self.subTest(pokemon=pokemon):
                self.assertIsInstance(pokemon, Pokemon)

    def test_verificando_se_os_pokemons_foram_adicionados_ao_objeto_inimigo(self):
        pokemons = InimigoFactory.get_inimigo().lista_pokemons
        self.assertGreaterEqual(len(pokemons), 1)

if __name__ == '__main__':
    unittest.main()
