# core_functionality.py
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

    def _resultado_da_batalha(self, vencedor: str, id_pokemon: int) -> None:
        """
        Método privado que configura o nível do pokemon do jogador
        caso ele ganhe.

        :param vencedor: Vencedor da luta. pode ser "Player" ou "Inimigo".
        :type vencedor: str
        :param id_pokemon: Indice do pokemon do jogador.
        :type id_pokemon: int

        :return: None
        :rtype: None
        """
        if vencedor == 'Player':
            self.lista_pokemons[id_pokemon].subir_nivel()
            print(f'VOCÊ!!! {self.nome} GANHOU A BATALHA!!!')
            print(f'Após vencer o seu pokemon subiu 2 leveis!!!!!!')
            return

        print('Infelizmente você perdeu, quem sabe na próxima! E por causa disso o seu pokemon não subiu de nível')
