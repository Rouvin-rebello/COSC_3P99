from pokemon import Pokemon

class Batalha:
    def __init__(self, pokemon: Pokemon, pokemon2: Pokemon) -> None:
        if not isinstance(pokemon, Pokemon) or not isinstance(pokemon2, Pokemon):
            raise ValueError("Os participantes devem ser instâncias da classe Pokemon")
        self.participante1: Pokemon = pokemon
        self.participante2: Pokemon = pokemon2
