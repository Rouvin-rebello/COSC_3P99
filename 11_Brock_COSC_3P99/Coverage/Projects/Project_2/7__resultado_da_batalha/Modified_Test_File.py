# test_all.py
import unittest
from core_functionality import Jogador
from pokemon import Pokemon
from boundary_conditions import test_boundary_conditions
from error_handling import test_error_handling
from ui_interactions import test_ui_interactions
from output_consistency import test_output_consistency

class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Pokemon(20)]

    def test_resultado_da_batalha_o_jogador_nao_ganhou_a_batalha(self):
        nivel_pokemon_que_lutou_antes_da_luta = self.jogador.lista_pokemons[0].nivel
        self.jogador._resultado_da_batalha('Inimigo', 0)
        self.assertEqual(nivel_pokemon_que_lutou_antes_da_luta,
                         self.jogador.lista_pokemons[0].nivel)

    def test_resultado_da_batalha_o_jogador_ganhou_a_batalha_upando_assim_o_pokemon(self):
        nivel_pokemon_que_lutou_antes_da_luta = self.jogador.lista_pokemons[0].nivel

        self.jogador._resultado_da_batalha('Player', 0)
        self.assertNotEqual(nivel_pokemon_que_lutou_antes_da_luta,
                            self.jogador.lista_pokemons[0].nivel)

    def test_boundary_conditions(self):
        test_boundary_conditions()

    def test_error_handling(self):
        test_error_handling()

    def test_ui_interactions(self):
        test_ui_interactions()

    def test_output_consistency(self):
        test_output_consistency()

if __name__ == '__main__':
    unittest.main()
