from core_functionality import Pokemon

class PokemonOutputConsistency(Pokemon):
    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(f'{self.__class__.__name__} atacou {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque
