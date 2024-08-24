import unittest
from Function_5_Source import Pessoa
from pokemon import Pokemon

class TestPessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.pessoa = Pessoa()
        self.pessoa.lista_pokemons = [Pokemon(), Pokemon()]

    def test_capturar_pokemon_deve_levantar_assertion_error_caso_parametro_nao_seja_um_objeto_do_tipo_pokemon(self):
        with self.assertRaises(AssertionError):
            self.pessoa.capturar_pokemon('pokemon')

    def test_capturar_pokemon_deve_adicionar_pokemon_a_lista_de_pokemons_caso_seja_objeto_do_tipo_pokemon(self):
        tamanho_lista = len(self.pessoa.lista_pokemons)
        self.pessoa.capturar_pokemon(Pokemon())
        self.assertEqual(tamanho_lista + 1, len(self.pessoa.lista_pokemons))

if __name__ == '__main__':
    unittest.main()
