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


from Project_2_Combined_Source import (AtaqueComForca, AtaqueComFraqueza,AtaqueStrategy)
from Project_2_Combined_Source import Batalha, Inimigo, InimigoFactory, Jogador, Pessoa, AtaqueNormal
from Project_2_Combined_Source import (Charmander, Magicarpa, Onix, Pikachu, Pokemon,
                     PokemonAgua, PokemonEletrico, PokemonFactory, PokemonFogo,
                     PokemonPedra)


class TestAtaqueComFraqueza(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_com_fraqueza = AtaqueComFraqueza()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_com_fraqueza.calcular_ataque(
            valor_ataque_base=10, level_atual=2), (float, int))


class TestAtaqueComForca(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_com_forca = AtaqueComForca()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_com_forca.calcular_ataque(
            valor_ataque_base=10, level_atual=2), (float, int))


class TestAtaqueNormal(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_normal = AtaqueNormal()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_normal.calcular_ataque(
            valor_ataque_base=10, level_atual=2), (float, int))

class TestBatalha(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_onix = Onix(1)
        self.pokemon_magicarpa = Magicarpa(1)
        self.pokemon_pikachu = Pikachu(1)
        self.pokemon_charmander = Charmander(1)
        self.batalha = Batalha(self.pokemon_onix, self.pokemon_magicarpa)

    def test_batalha_attr_participante1_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante1, self.pokemon_onix)

    def test_batalha_attr_participante2_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante2, self.pokemon_magicarpa)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante1_da_luta(self):
        self.assertIsInstance(
            self.batalha.participante1.estrategia_luta, AtaqueStrategy)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante2_da_luta(self):
        self.assertIsInstance(
            self.batalha.participante2.estrategia_luta, AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_um_objeto_do_tipo_estrategia_de_ataque(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_pedra_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_agua_enfrenta_pokemon_eletrico(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_magicarpa,
                                                        pokemon2=self.pokemon_pikachu), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_eletrico_enfrenta_pokemon_pedra(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_pikachu,
                                                        pokemon2=self.pokemon_onix), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_fogo_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_charmander,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_pedra_enfrenta_pokemon_eletrico(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_pikachu), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_eletrico_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_pikachu,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_agua_enfrenta_pokemon_fogo(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_magicarpa,
                                                        pokemon2=self.pokemon_charmander), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_fogo_enfrenta_pokemon_pedra(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_charmander,
                                                        pokemon2=self.pokemon_onix), AtaqueComForca)

    def test_definir_vantagens_retorna_ataque_normal_quando_um_pokemon_enfrenta_outro_que_o_elemento_nao_interfere(
            self):
        sem_vantagem_no_combate = [(self.pokemon_onix, self.pokemon_onix),
                                   (self.pokemon_onix, self.pokemon_charmander),
                                   (self.pokemon_pikachu, self.pokemon_pikachu),
                                   (self.pokemon_pikachu, self.pokemon_charmander),
                                   (self.pokemon_magicarpa,
                                    self.pokemon_magicarpa),
                                   (self.pokemon_magicarpa, self.pokemon_onix),
                                   (self.pokemon_charmander,
                                    self.pokemon_charmander),
                                   (self.pokemon_charmander, self.pokemon_pikachu)
                                   ]
        for pokemon1, pokemon2 in sem_vantagem_no_combate:
            with self.subTest(pokemon1=pokemon1, pokemon2=pokemon2):
                self.assertIsInstance(Batalha.definir_vantagens(
                    pokemon1=pokemon1, pokemon2=pokemon2), AtaqueNormal)

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
        self.assertEqual(vida_pikachu_antes_da_luta,
                         batalha_teste.participante1.vida)
        self.assertEqual(vida_onix_antes_da_luta,
                         batalha_teste.participante2.vida)

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


class TestInimigo(unittest.TestCase):
    def setUp(self) -> None:
        self.inimigo = Inimigo()

    def test_inimigo_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.inimigo.nome, 'Desconhecido')

    def test_inimigo_attr_lista_pokemons_foi_inicializado_corretamente(self):
        self.assertIsInstance(self.inimigo.lista_pokemons, list)
        self.assertEqual(len(self.inimigo.lista_pokemons), 0)


class TestInimigoFactory(unittest.TestCase):
    def test_verificando_o_retorno_se_e_um_objeto_do_tipo_inimigo(self):
        self.assertIsInstance(InimigoFactory.get_inimigo(), Inimigo)

    def test_verificando_se_os_pokemons_adicionados_ao_objeto_inimigo_sao_realmente_objetos_do_tipo_pokemon(self):
        pokemons = [
            pokemon for pokemon in InimigoFactory.get_inimigo().lista_pokemons]

        for pokemon in pokemons:
            with self.subTest(pokemon=pokemon):
                self.assertIsInstance(pokemon, Pokemon)

    def test_verificando_se_os_pokemons_foram_adicionados_ao_objeto_inimigo(self):
        pokemons = InimigoFactory.get_inimigo().lista_pokemons
        self.assertGreaterEqual(len(pokemons), 1)


class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Onix(20)]
        self.inimigo = Inimigo()
        self.inimigo.lista_pokemons = [Onix(10), Charmander(2)]
        self.pessoa = Pessoa()

    def test_jogador_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.jogador.nome, 'walex')

    def test_batalhar_deve_levantar_uma_assertion_error_caso_quem_ele_enfrente_nao_seja_um_objeto_do_tipo_inimigo(self):
        with self.assertRaises(AssertionError):
            self.jogador.batalhar(
                id_pokemon=0, inimigo=self.pessoa, id_pokemon_inimigo=1)

    def test_batalhar_deve_retornar_false_caso_o_id_de_pokemon_nao_seja_um_indice_valido_para_a_lista_pokemons_do_jogador(self):
        indices_invalidos = (-5, -2, -1, len(self.jogador.lista_pokemons) + 1)

        for indice_invalido in indices_invalidos:
            with self.subTest(indice_invalido=indice_invalido):
                self.assertFalse(
                    self.jogador.batalhar(id_pokemon=indice_invalido, inimigo=self.inimigo, id_pokemon_inimigo=1))

    def test_batalhar_conseguiu_realizar_a_batalha_com_sucesso(self):
        self.assertTrue(self.jogador.batalhar(
            id_pokemon=0, inimigo=self.inimigo, id_pokemon_inimigo=1))

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
        self.assertNotEqual(self.pokemon.ataque_base,
                            ataque_base_antes_pokemon)


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

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.onix.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestCharmander(unittest.TestCase):
    def setUp(self) -> None:
        self.charmander = Charmander(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.charmander.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestPikachu(unittest.TestCase):
    def setUp(self) -> None:
        self.pikachu = Pikachu(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.pikachu.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestMagicarpa(unittest.TestCase):
    def setUp(self) -> None:
        self.magicarpa = Magicarpa(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.magicarpa.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestPokemonFactory(unittest.TestCase):
    def test_get_pokemon_esta_retornando_um_objeto_do_tipo_pokemon(self):
        self.assertIsInstance(PokemonFactory.get_pokemon(), Pokemon)