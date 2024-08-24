import random
from pokemon import Onix, Charmander, Magicarpa, Pikachu, Pokemon

class PokemonFactory:
    @staticmethod
    def get_pokemon(nome: str = None, nivel: int = None) -> Pokemon:
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
