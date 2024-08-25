from ataque import AtaqueNormal, AtaqueStrategy

class Pokemon:
    tipo: str
    fraqueza: str
    forte_contra: str

    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel
        self.estrategia_luta: AtaqueStrategy = AtaqueNormal()

    def subir_nivel(self) -> None:
        self.nivel += 2
        self._reconfigurar_status()

    def _reconfigurar_status(self) -> None:
        self.vida = 10 * self.nivel
        self.ataque_base = 4 * self.nivel

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

# Subclasses of Pokemon
class PokemonFogo(Pokemon):
    tipo = 'FOGO'
    fraqueza = 'AGUA'
    forte_contra = 'PEDRA'

class PokemonAgua(Pokemon):
    tipo = 'AGUA'
    fraqueza = 'ELETRICO'
    forte_contra = 'FOGO'

class PokemonEletrico(Pokemon):
    tipo = 'ELETRICO'
    fraqueza = 'PEDRA'
    forte_contra = 'AGUA'

class PokemonPedra(Pokemon):
    tipo = 'PEDRA'
    fraqueza = 'AGUA'
    forte_contra = 'ELETRICO'

# Example Pokemon classes with specific attacks
class Onix(PokemonPedra):
    def atacar(self, pokemon: Pokemon) -> None:
        dano_ataque = self.ataque_base
        print(f'Onix deu uma rabada no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque

class Charmander(PokemonFogo):
    def atacar(self, pokemon: Pokemon) -> None:
        dano_ataque = self.ataque_base
        print(f'Charmander lançou um assopro de fogo no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque

class Pikachu(PokemonEletrico):
    def atacar(self, pokemon: Pokemon) -> None:
        dano_ataque = self.ataque_base
        print(f'Pikachu usou o choque do TROVÃO!!! no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque

class Magicarpa(PokemonAgua):
    def atacar(self, pokemon: Pokemon) -> None:
        dano_ataque = self.ataque_base
        print(f'Magicarpa deu uma cuspida fraca :/ no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque
