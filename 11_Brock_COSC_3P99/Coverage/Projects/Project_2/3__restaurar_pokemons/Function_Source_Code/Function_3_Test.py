import unittest
from pokemon import Onix, Pikachu
from Function_3_Source import Batalha

class TestRestaurarPokemons(unittest.TestCase):
    def test_batalhar_verifica_se_a_vida_dos_pokemons_foi_restaurada_apos_a_luta(self):
        onix = Onix(50)
        pikachu = Pikachu(1)
        vida_pikachu_antes_da_luta = pikachu.vida
        vida_onix_antes_da_luta = onix.vida
        batalha_teste = Batalha(pikachu, onix)
        batalha_teste._restaurar_pokemons()
        self.assertEqual(vida_pikachu_antes_da_luta, batalha_teste.participante1.vida)
        self.assertEqual(vida_onix_antes_da_luta, batalha_teste.participante2.vida)

if __name__ == '__main__':
    unittest.main()
