from core_functionality import Pokemon

class PokemonUIInteractions(Pokemon):
    def apresentar_pokemon(self) -> None:
        print(f'pokemon: {self.__class__.__name__}')
        print(f'Level: {self.nivel}')
        print(f'Vida: {self.vida} de pontos.')
        print(f'Dano base: {self.ataque_base}')
