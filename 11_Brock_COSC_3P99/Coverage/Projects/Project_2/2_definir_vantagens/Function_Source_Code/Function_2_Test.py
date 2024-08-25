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
from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy
from pokemon import Charmander, Magicarpa, Onix, Pikachu
from Function_2_Source import definir_vantagens

class TestDefinirVantagens(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_onix = Onix(1)
        self.pokemon_magicarpa = Magicarpa(1)
        self.pokemon_pikachu = Pikachu(1)
        self.pokemon_charmander = Charmander(1)

    def test_definir_vantagens_verifica_se_retorna_um_objeto_do_tipo_estrategia_de_ataque(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_onix, pokemon2=self.pokemon_magicarpa), AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_pedra_enfrenta_pokemon_agua(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_onix, pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_agua_enfrenta_pokemon_eletrico(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_magicarpa, pokemon2=self.pokemon_pikachu), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_eletrico_enfrenta_pokemon_pedra(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_pikachu, pokemon2=self.pokemon_onix), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_fogo_enfrenta_pokemon_agua(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_charmander, pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_pedra_enfrenta_pokemon_eletrico(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_onix, pokemon2=self.pokemon_pikachu), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_eletrico_enfrenta_pokemon_agua(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_pikachu, pokemon2=self.pokemon_magicarpa), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_agua_enfrenta_pokemon_fogo(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_magicarpa, pokemon2=self.pokemon_charmander), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_fogo_enfrenta_pokemon_pedra(self):
        self.assertIsInstance(definir_vantagens(pokemon1=self.pokemon_charmander, pokemon2=self.pokemon_onix), AtaqueComForca)

    def test_definir_vantagens_retorna_ataque_normal_quando_um_pokemon_enfrenta_outro_que_o_elemento_nao_interfere(self):
        sem_vantagem_no_combate = [
            (self.pokemon_onix, self.pokemon_onix),
            (self.pokemon_onix, self.pokemon_charmander),
            (self.pokemon_pikachu, self.pokemon_pikachu),
            (self.pokemon_pikachu, self.pokemon_charmander),
            (self.pokemon_magicarpa, self.pokemon_magicarpa),
            (self.pokemon_magicarpa, self.pokemon_onix),
            (self.pokemon_charmander, self.pokemon_charmander),
            (self.pokemon_charmander, self.pokemon_pikachu)
        ]
        for pokemon1, pokemon2 in sem_vantagem_no_combate:
            with self.subTest(pokemon1=pokemon1, pokemon2=pokemon2):
                self.assertIsInstance(definir_vantagens(pokemon1=pokemon1, pokemon2=pokemon2), AtaqueNormal)

if __name__ == '__main__':
    unittest.main()
