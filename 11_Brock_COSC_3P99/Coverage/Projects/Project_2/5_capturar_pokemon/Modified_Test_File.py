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


# test_all.py
import unittest
from core_functionality import Pessoa
from pokemon import Pokemon
from boundary_conditions import test_boundary_conditions
from error_handling import test_error_handling
from output_consistency import test_output_consistency

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

    def test_boundary_conditions(self):
        test_boundary_conditions()

    def test_error_handling(self):
        test_error_handling()

    def test_output_consistency(self):
        test_output_consistency()

if __name__ == '__main__':
    unittest.main()
