from typing import List
from pokemon import Pokemon

class Jogador:
    """
    Classe responsável pela configuração do jogador e funcionalidades do mesmo.

    Atributos:
    nome (str): Nome do jogador.
    lista_pokemons (List[Pokemon]): Lista de pokemons do jogador.
    """

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.lista_pokemons: List[Pokemon] = []

    def apresentar_pokemons(self) -> None:
        """Apresenta os pokemons do jogador antes da luta.
        :return: None
        :rtype: None
        """
        for indice, pokemon in enumerate(self.lista_pokemons):
            print(f'Digite = {indice} para escolher o/a {pokemon.__class__.__name__} de nível {pokemon.nivel} e dano '
                  f'base de {pokemon.ataque_base}')
