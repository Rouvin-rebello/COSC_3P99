# test_all.py
import unittest
from core_functionality import Batalha
from integration_points import create_pokemon_instances
from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy
from pokemon import Charmander, Magicarpa, Onix, Pikachu
from output_consistency import test_batalhar_output

class TestBatalha(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_onix, self.pokemon_magicarpa, self.pokemon_pikachu, self.pokemon_charmander = create_pokemon_instances()
        self.batalha = Batalha(self.pokemon_onix, self.pokemon_magicarpa)

    def test_batalha_attr_participante1_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante1, self.pokemon_onix)

    def test_batalha_attr_participante2_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante2, self.pokemon_magicarpa)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante1_da_luta(self):
        self.assertIsInstance(self.batalha.participante1.estrategia_luta, AtaqueStrategy)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante2_da_luta(self):
        self.assertIsInstance(self.batalha.participante2.estrategia_luta, AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_um_objeto_do_tipo_estrategia_de_ataque(self):
        self.assertIsInstance(Batalha.definir_vantagens(self.pokemon_onix, self.pokemon_magicarpa), AtaqueStrategy)

    def test_batalhar_verifica_se_retorna_player_quando_o_jogador_vence_o_inimigo(self):
        batalha_teste = Batalha(Onix(50), Pikachu(1))
        self.assertEqual(batalha_teste.batalhar(), 'Player')

    def test_batalhar_verifica_se_retorna_inimigo_quando_o_jogador_perde_para_o_inimigo(self):
        batalha_teste = Batalha(Pikachu(1), Onix(50))
        self.assertEqual(batalha_teste.batalhar(), 'Inimigo')

    def test_batalhar_verifica_se_a_vida_dos_pokemons_foi_restaurada_apos_a_luta(self):
        onix = Onix(50)
        pikachu = Pikachu(1)
        vida_pikachu_antes_da_luta = pikachu.vida
        vida_onix_antes_da_luta = onix.vida
        batalha_teste = Batalha(pikachu, onix)
        batalha_teste.batalhar()
        self.assertEqual(vida_pikachu_antes_da_luta, batalha_teste.participante1.vida)
        self.assertEqual(vida_onix_antes_da_luta, batalha_teste.participante2.vida)

    def test_output_consistency(self):
        test_batalhar_output()

if __name__ == '__main__':
    unittest.main()
