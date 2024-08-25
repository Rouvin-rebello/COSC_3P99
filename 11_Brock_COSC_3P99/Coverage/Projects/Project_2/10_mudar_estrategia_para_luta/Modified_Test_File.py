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
from ataque import AtaqueStrategy, AtaqueNormal
from core_functionality import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_mudar_estrategia_para_luta_deve_levantar_assertion_caso_o_argumento_passado_nao_seja_do_tipo_ataque_strategy(self):
        with self.assertRaises(AssertionError):
            self.pokemon.mudar_estrategia_para_luta('estrategia')

    def test_mudar_estrategia_para_luta_deve_atualizar_a_estrategia_luta(self):
        nova_estrategia = AtaqueNormal()
        self.pokemon.mudar_estrategia_para_luta(nova_estrategia)
        self.assertEqual(self.pokemon.estrategia_luta, nova_estrategia)

if __name__ == "__main__":
    unittest.main()
