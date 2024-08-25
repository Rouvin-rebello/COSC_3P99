import unittest
from core_functionality import definir_vantagens
from pokemon import Charmander, Magicarpa, Onix, Pikachu
from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy

class TestCoreFunctionality(unittest.TestCase):
    def setUp(self):
        self.pokemon_onix = Onix(1)
        self.pokemon_magicarpa = Magicarpa(1)
        self.pokemon_pikachu = Pikachu(1)
        self.pokemon_charmander = Charmander(1)

    def test_definir_vantagens(self):
        self.assertIsInstance(definir_vantagens(self.pokemon_onix, self.pokemon_magicarpa), AtaqueStrategy)

if __name__ == '__main__':
    unittest.main()
