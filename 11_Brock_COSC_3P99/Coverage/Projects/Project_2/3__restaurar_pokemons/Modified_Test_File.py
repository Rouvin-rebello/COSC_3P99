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
from core_functionality import Batalha
from boundary_conditions import verificar_vida_restaurada
from error_handling import Batalha as BatalhaErrorHandling
from output_consistency import Batalha as BatalhaOutputConsistency
from pokemon import Onix, Pikachu

class TestBatalha(unittest.TestCase):

    def setUp(self):
        self.onix = Onix(50)
        self.pikachu = Pikachu(1)

    def test_batalha_inicializacao(self):
        batalha = Batalha(self.pikachu, self.onix)
        self.assertEqual(batalha.participante1, self.pikachu)
        self.assertEqual(batalha.participante2, self.onix)

class TestRestaurarPokemons(unittest.TestCase):

    def setUp(self):
        self.onix = Onix(50)
        self.pikachu = Pikachu(1)

    def test_restaurar_pokemons(self):
        vida_pikachu_antes_da_luta = self.pikachu.vida
        vida_onix_antes_da_luta = self.onix.vida
        batalha = BatalhaOutputConsistency(self.pikachu, self.onix)
        batalha._restaurar_pokemons()
        self.assertEqual(vida_pikachu_antes_da_luta, batalha.participante1.vida)
        self.assertEqual(vida_onix_antes_da_luta, batalha.participante2.vida)

class TestBoundaryConditions(unittest.TestCase):

    def setUp(self):
        self.onix = Onix(50)
        self.pikachu = Pikachu(1)

    def test_verificar_vida_restaurada(self):
        batalha = BatalhaOutputConsistency(self.pikachu, self.onix)
        batalha._restaurar_pokemons()
        self.assertTrue(verificar_vida_restaurada(batalha.participante1, batalha.participante2))

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.onix = Onix(50)
        self.pikachu = Pikachu(1)

    def test_batalha_inicializacao_com_erro(self):
        with self.assertRaises(ValueError):
            BatalhaErrorHandling("invalid", self.onix)
        with self.assertRaises(ValueError):
            BatalhaErrorHandling(self.pikachu, "invalid")

if __name__ == '__main__':
    unittest.main()
