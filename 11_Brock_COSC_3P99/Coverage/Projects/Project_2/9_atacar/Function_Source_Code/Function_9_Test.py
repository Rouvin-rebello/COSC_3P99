import unittest
from Function_9_Source import Charmander, Magicarpa, Onix, Pikachu, Pokemon, PokemonAgua, PokemonEletrico, PokemonFogo, PokemonPedra
from ataque import AtaqueNormal

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_pokemon_attr_nivel_tem_o_valor_correto(self):
        self.assertEqual(self.pokemon.nivel, self.nivel_pokemon)

    def test_pokemon_attr_vida_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.vida, self.nivel_pokemon * 10)

    def test_pokemon_attr_ataque_base_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.ataque_base, self.nivel_pokemon * 4)

    def test_pokemon_attr_estrategia_luta_foi_inicializado_com_objeto_ataque_normal(self):
        self.assertIsInstance(self.pokemon.estrategia_luta, AtaqueNormal)

    def test_atacar_deve_levantar_assertion_caso_o_parametro_nao_seja_um_pokemon(self):
        with self.assertRaises(AssertionError):
            self.pokemon.atacar('pokemon')

    def test_mudar_estrategia_para_luta_deve_levantar_assertion_caso_o_argumento_passado_nao_seja_do_tipo_ataque_strategy(self):
        with self.assertRaises(AssertionError):
            self.pokemon.mudar_estrategia_para_luta('estrategia')

    def test_ataque_retorna_o_valor_de_ataque_em_float(self):
        self.assertIsInstance(self.pokemon.ataque, float)

    def test_recuperar_vida_esta_restaurando_a_vida_corretamente_de_acordo_com_o_seu_level(self):
        vida_completa_pokemon = self.pokemon.vida
        self.pokemon.vida -= 20
        self.pokemon.recuperar_vida()
        self.assertEqual(vida_completa_pokemon, self.pokemon.vida)

    def test_subir_nivel_deve_aumentar_o_attr_nivel_do_pokemon(self):
        nivel_antes_de_subir = self.pokemon.nivel
        self.pokemon.subir_nivel()
        self.assertEqual(nivel_antes_de_subir + 2, self.pokemon.nivel)

    def test_reconfigurar_status_deve_reconfigurar_todos_os_attr_de_acordo_com_o_novo_nivel(self):
        vida_antes_pokemon = self.pokemon.vida
        ataque_base_antes_pokemon = self.pokemon.ataque_base
        self.pokemon.subir_nivel()
        self.assertNotEqual(self.pokemon.vida, vida_antes_pokemon)
        self.assertNotEqual(self.pokemon.ataque_base, ataque_base_antes_pokemon)

class TestPokemonAgua(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_agua = PokemonAgua(5)

    def test_pokemon_agua_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_agua.tipo, 'AGUA')

    def test_pokemon_agua_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_agua.fraqueza, 'ELETRICO')

    def test_pokemon_agua_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_agua.forte_contra, 'FOGO')

class TestPokemonFogo(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_fogo = PokemonFogo(5)

    def test_pokemon_fogo_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_fogo.tipo, 'FOGO')

    def test_pokemon_fogo_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_fogo.fraqueza, 'AGUA')

    def test_pokemon_fogo_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_fogo.forte_contra, 'PEDRA')

class TestPokemonEletrico(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_eletrico = PokemonEletrico(5)

    def test_pokemon_eletrico_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.tipo, 'ELETRICO')

    def test_pokemon_eletrico_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.fraqueza, 'PEDRA')

    def test_pokemon_eletrico_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.forte_contra, 'AGUA')

class TestPokemonPedra(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_pedra = PokemonPedra(5)

    def test_pokemon_pedra_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_pedra.tipo, 'PEDRA')

    def test_pokemon_pedra_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_pedra.fraqueza, 'AGUA')

    def test_pokemon_pedra_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_pedra.forte_contra, 'ELETRICO')

class TestOnix(unittest.TestCase):
    def setUp(self) -> None:
        self.onix = Onix(5)
        self.charmander = Charmander(5)

    def test_onix_instance_of_pokemon_pedra(self):
        self.assertIsInstance(self.onix, PokemonPedra)

    def test_onix_instance_of_pokemon(self):
        self.assertIsInstance(self.onix, Pokemon)

    def test_onix_esta_removendo_a_quantidade_correta_de_vida_quando_ataca(self):
        vida_antes_ataque = self.charmander.vida
        self.onix.atacar(self.charmander)
        self.assertEqual(self.charmander.vida, vida_antes_ataque - self.onix.ataque)

class TestCharmander(unittest.TestCase):
    def setUp(self) -> None:
        self.charmander = Charmander(5)
        self.pikachu = Pikachu(5)

    def test_charmander_instance_of_pokemon_fogo(self):
        self.assertIsInstance(self.charmander, PokemonFogo)

    def test_charmander_instance_of_pokemon(self):
        self.assertIsInstance(self.charmander, Pokemon)

    def test_charmander_esta_removendo_a_quantidade_correta_de_vida_quando_ataca(self):
        vida_antes_ataque = self.pikachu.vida
        self.charmander.atacar(self.pikachu)
        self.assertEqual(self.pikachu.vida, vida_antes_ataque - self.charmander.ataque)

class TestPikachu(unittest.TestCase):
    def setUp(self) -> None:
        self.pikachu = Pikachu(5)
        self.magicarpa = Magicarpa(5)

    def test_pikachu_instance_of_pokemon_eletrico(self):
        self.assertIsInstance(self.pikachu, PokemonEletrico)

    def test_pikachu_instance_of_pokemon(self):
        self.assertIsInstance(self.pikachu, Pokemon)

    def test_pikachu_esta_removendo_a_quantidade_correta_de_vida_quando_ataca(self):
        vida_antes_ataque = self.magicarpa.vida
        self.pikachu.atacar(self.magicarpa)
        self.assertEqual(self.magicarpa.vida, vida_antes_ataque - self.pikachu.ataque)

class TestMagicarpa(unittest.TestCase):
    def setUp(self) -> None:
        self.magicarpa = Magicarpa(5)
        self.onix = Onix(5)

    def test_magicarpa_instance_of_pokemon_agua(self):
        self.assertIsInstance(self.magicarpa, PokemonAgua)

    def test_magicarpa_instance_of_pokemon(self):
        self.assertIsInstance(self.magicarpa, Pokemon)

    def test_magicarpa_esta_removendo_a_quantidade_correta_de_vida_quando_ataca(self):
        vida_antes_ataque = self.onix.vida
        self.magicarpa.atacar(self.onix)
        self.assertEqual(self.onix.vida, vida_antes_ataque - self.magicarpa.ataque)

if __name__ == '__main__':
    unittest.main()
