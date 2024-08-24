import unittest
from Function_7_Source import Jogador
from pokemon import Onix


class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Onix(20)]

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


if __name__ == '__main__':
    unittest.main()
