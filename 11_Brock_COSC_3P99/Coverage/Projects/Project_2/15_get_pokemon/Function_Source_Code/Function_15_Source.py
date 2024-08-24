import random
from ataque import AtaqueStrategy, AtaqueNormal
from pokemon import Onix, Charmander, Magicarpa, Pikachu, Pokemon


class PokemonFactory:
    """
    Classe fábrica de pokemon responsável por gerar pokemons a serem
    capturados por inimigos e jogadores.
    """

    @staticmethod
    def get_pokemon(nome: str = None, nivel: int = None) -> Pokemon:
        """
        Método responsável por retornar um pokemon aleatório ou
        de acordo com os parâmetros passados.

        :param nome: Nome do pokemon desejado. (opcional)
        :type nome: str
        :param nivel: Nível do pokemon desejado. (opcional)
        :type nivel: int

        :return: Retorna o pokemon aleatorio ou de acordo com os parâmetros.
        :rtype: Pokemon
        """
        nivel_aleatorio = nivel or random.randint(1, 100)
        pokemon = nome or random.choice(
            ['onix', 'charmander', 'magicarpa', 'pikachu'])

        if pokemon.lower() == 'onix':
            return Onix(nivel_aleatorio)
        if pokemon.lower() == 'charmander':
            return Charmander(nivel_aleatorio)
        if pokemon.lower() == 'magicarpa':
            return Magicarpa(nivel_aleatorio)
        if pokemon.lower() == 'pikachu':
            return Pikachu(nivel_aleatorio)
