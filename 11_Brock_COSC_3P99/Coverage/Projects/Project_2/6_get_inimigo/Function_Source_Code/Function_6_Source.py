from __future__ import annotations
import random
from typing import List
from pokemon import Pokemon, PokemonFactory

class Pessoa:
    """ Classe abstrata """
    lista_pokemons: List[Pokemon]
    nome: str

    def capturar_pokemon(self, pokemon: Pokemon) -> None:
        """
        Método responsável por adicionar o pokemon na lista_pokemons da pessoa.
        :param pokemon: Pokemon que será adicionado a lista.
        :type pokemon: Pokemon
        :raise AssertionError: paramêtro pokemon não ser um objeto do tipo pokemon.
        :return: None
        :rtype: None
        """
        assert isinstance(pokemon, Pokemon), 'O objeto precisa ser um Pokemon'
        self.lista_pokemons.append(pokemon)

class Inimigo(Pessoa):
    """
    Classe responsável pela gerenciamento do inimigo.
    Atributos:
    nome (str): Nome do inimigo. sempre será ("Desconhecido").
    lista_pokemons (List[Pokemon]): Lista de pokemons do inimigo.
    """

    def __init__(self) -> None:
        self.nome: str = 'Desconhecido'
        self.lista_pokemons: List[Pokemon] = []

class InimigoFactory:
    """
    Classe fábrica responsável por gerar inimigos para o jogo.
    """
    @staticmethod
    def get_inimigo() -> Inimigo:
        """
        Método responsável por gerar um inimigo para o jogo, gerando aleatoriamente de 1 a 4 pokemons para ele.
        :return: Retorna o inimigo que o jogador vai enfrentar.
        :rtype: Inimigo
        """
        quantidade_de_pokemons = random.randint(1, 4)
        inimigo = Inimigo()
        for _ in range(quantidade_de_pokemons):
            inimigo.capturar_pokemon(PokemonFactory.get_pokemon())

        return inimigo
