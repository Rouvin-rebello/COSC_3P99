"""
This module defines the function to determine attack strategies
based on the types of two Pokemon.
"""

from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy
from pokemon import Pokemon

def definir_vantagens(pokemon1: Pokemon, pokemon2: Pokemon) -> AtaqueStrategy:
    """
    Método responsável por definir a estrategia de ataque de determinado
    pokemon baseando no seu tipo e no tipo do pokemon inimigo.

    :param pokemon1: Pokemon que vai atacar.
    :type pokemon1: Pokemon
    :param pokemon2: Pokemon que vai enfrentar o pokemon1.
    :type pokemon2: Pokemon

    :return: Retorna uma classe do tipo AtaqueStrategy de acordo com os tipos dos pokemons
    :rtype: AtaqueStrategy
    """
    if pokemon1.fraqueza == pokemon2.tipo:
        print(f'{pokemon1} está em desvantagem na luta contra {pokemon2}')
        return AtaqueComFraqueza()

    if pokemon1.forte_contra == pokemon2.tipo:
        print(f'{pokemon1} está em vantagem na luta contra {pokemon2}')
        return AtaqueComForca()

    print(f'Parece que o/a {pokemon1} não tem nenhuma vantagem sobre {pokemon2}')
    return AtaqueNormal()
