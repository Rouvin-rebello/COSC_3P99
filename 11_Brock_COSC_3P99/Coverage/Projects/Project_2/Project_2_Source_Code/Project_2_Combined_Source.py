import random
from abc import ABC, abstractmethod
from typing import List


class AtaqueStrategy(ABC):
    """Class Interface de ataque"""
    @abstractmethod
    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        pass


class AtaqueComFraqueza(AtaqueStrategy):
    """Classe com estrategia de ataque com valor reduzido"""

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base - (valor_ataque_base * 0.25) + level_atual) * fator_sorte


class AtaqueNormal(AtaqueStrategy):
    """Classe com estrategia de ataque com valor normal"""

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base + level_atual) * fator_sorte


class AtaqueComForca(AtaqueStrategy):
    """Classe com estrategia de ataque com valor potencializado"""

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base + (valor_ataque_base * 0.45) + level_atual) * fator_sorte


class Batalha:
    """Classe responsável por organizar e realizar a batalha entre dois pokemons diferentes."""

    def __init__(self, pokemon, pokemon2) -> None:
        self.participante1 = pokemon
        self.participante2 = pokemon2

        self.participante1.mudar_estrategia_para_luta(self.definir_vantagens(pokemon, self.participante2))
        self.participante2.mudar_estrategia_para_luta(self.definir_vantagens(pokemon2, self.participante1))

    @staticmethod
    def definir_vantagens(pokemon1, pokemon2) -> AtaqueStrategy:
        if pokemon1.fraqueza == pokemon2.tipo:
            print(f'{pokemon1} está em desvantagem na luta contra {pokemon2}')
            return AtaqueComFraqueza()

        if pokemon1.forte_contra == pokemon2.tipo:
            print(f'{pokemon1} está em vantagem na luta contra {pokemon2}')
            return AtaqueComForca()

        print(f'Parece que o/a {pokemon1} não tem nenhuma vantagem sobre {pokemon2}')
        return AtaqueNormal()

    def _restaurar_pokemons(self) -> None:
        self.participante1.recuperar_vida()
        self.participante2.recuperar_vida()

    def batalhar(self) -> str:
        while True:
            print('-' * 100)
            print(f'Vida do seu pokemon: {self.participante1}: {round(self.participante1.vida, 2)}')
            print(f'Vida de {self.participante2}: {round(self.participante2.vida, 2)}')

            self.participante1.atacar(self.participante2)

            if self.participante2.vida <= 0:
                print(self.participante1, 'é o vencedor')
                self._restaurar_pokemons()
                return 'Player'

            self.participante2.atacar(self.participante1)

            if self.participante1.vida <= 0:
                print(self.participante2, 'é o vencedor')
                self._restaurar_pokemons()
                return 'Inimigo'


class Pessoa:
    """Classe abstrata"""
    lista_pokemons: List
    nome: str

    def capturar_pokemon(self, pokemon) -> None:
        assert isinstance(pokemon, Pokemon), 'O objeto precisa ser um Pokemon'
        self.lista_pokemons.append(pokemon)

    def __str__(self) -> str:
        return f'{self.nome}'


class Inimigo(Pessoa):
    """Classe responsável pela gerenciamento do inimigo."""

    def __init__(self) -> None:
        self.nome = 'Desconhecido'
        self.lista_pokemons = []


class InimigoFactory:
    """Classe fábrica responsável por gerar inimigos para o jogo."""

    @staticmethod
    def get_inimigo() -> Inimigo:
        quantidade_de_pokemons = random.randint(1, 4)
        inimigo = Inimigo()
        for i in range(quantidade_de_pokemons):
            inimigo.capturar_pokemon(PokemonFactory.get_pokemon())
        return inimigo


class Jogador(Pessoa):
    """Classe responsável pela configuração do jogador e funcionalidades do mesmo."""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.lista_pokemons = []

    def batalhar(self, id_pokemon: int, inimigo: Inimigo, id_pokemon_inimigo: int) -> bool:
        assert isinstance(inimigo, Inimigo), 'Para batalhar precisa ser objeto do tipo Inimigo'

        if id_pokemon >= len(self.lista_pokemons) or id_pokemon < 0:
            return False

        print('#' * 50)
        print(f'{self.lista_pokemons[id_pokemon]} EU ESCOLHO VOCÊ!!!!')
        print('#' * 50)
        batalha = Batalha(self.lista_pokemons[id_pokemon], inimigo.lista_pokemons[id_pokemon_inimigo])

        self._resultado_da_batalha(batalha.batalhar(), id_pokemon)
        return True

    def _resultado_da_batalha(self, vencedor: str, id_pokemon: int) -> None:
        if vencedor == 'Player':
            self.lista_pokemons[id_pokemon].subir_nivel()
            print(f'VOCÊ!!! {self.nome} GANHOU A BATALHA!!!')
            print(f'Após vencer o seu pokemon subiu 2 leveis!!!!!!')
        else:
            print('Infelizmente você perdeu, quem sabe na próxima! E por causa disso o seu pokemon não subiu de nível')

    def apresentar_pokemons(self) -> None:
        for indice, pokemon in enumerate(self.lista_pokemons):
            print(f'Digite = {indice} para escolher o/a {pokemon.__class__.__name__} de nível {pokemon.nivel} e dano base de {pokemon.ataque_base}')


class Pokemon:
    """Classe abstrata pokemon responsável por configurar o comportamento genérico de todos os pokemons."""
    tipo: str
    fraqueza: str
    forte_contra: str

    def __init__(self, nivel: int = 5) -> None:
        self.nivel = nivel
        self.vida = 10 * nivel
        self.ataque_base = 4 * nivel
        self.estrategia_luta = AtaqueNormal()

    def atacar(self, pokemon) -> None:
        assert isinstance(pokemon, Pokemon), 'Objeto precisa ser do tipo Pokemon'

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        assert isinstance(estrategia, AtaqueStrategy), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia

    @property
    def ataque(self) -> float:
        return round(self.estrategia_luta.calcular_ataque(self.ataque_base, self.nivel), 1)

    def recuperar_vida(self) -> None:
        self.vida = 10 * self.nivel

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def subir_nivel(self) -> None:
        self.nivel += 2
        self._reconfigurar_status()

    def _reconfigurar_status(self) -> None:
        self.vida = 10 * self.nivel
        self.ataque_base = 4 * self.nivel

    def apresentar_pokemon(self) -> None:
        print(f'pokemon: {self.__class__.__name__}')
        print(f'Level: {self.nivel}')
        print(f'Vida: {self.vida} de pontos.')
        print(f'Dano base: {self.ataque_base}')


class PokemonFogo(Pokemon):
    """Classe abstrata para os pokemons do tipo Fogo."""
    tipo = 'FOGO'
    fraqueza = 'AGUA'
    forte_contra = 'PEDRA'


class PokemonAgua(Pokemon):
    """Classe abstrata para os pokemons do tipo Água."""
    tipo = 'AGUA'
    fraqueza = 'ELETRICO'
    forte_contra = 'FOGO'


class PokemonEletrico(Pokemon):
    """Classe abstrata para os pokemons do tipo Elétrico."""
    tipo = 'ELETRICO'
    fraqueza = 'PEDRA'
    forte_contra = 'AGUA'


class PokemonPedra(Pokemon):
    """Classe abstrata para os pokemons do tipo Pedra."""
    tipo = 'PEDRA'
    fraqueza = 'AGUA'
    forte_contra = 'ELETRICO'


class Onix(PokemonPedra):
    """Classe concreta pokemon Onix que herda da classe PokemonPedra."""

    def atacar(self, pokemon) -> None:
        super().atacar(pokemon)
        dano = self.ataque
        pokemon.vida -= dano
        print(f'{self} atacou com {dano} de dano!')


class Pikachu(PokemonEletrico):
    """Classe concreta pokemon Pikachu que herda da classe PokemonEletrico."""

    def atacar(self, pokemon) -> None:
        super().atacar(pokemon)
        dano = self.ataque
        pokemon.vida -= dano
        print(f'{self} atacou com {dano} de dano!')


class Magicarpa(PokemonAgua):
    """Classe concreta pokemon Magicarpa que herda da classe PokemonAgua."""

    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(f'Magicarpa deu uma cuspida fraca :/ no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque

class Squirtle(PokemonAgua):
    """Classe concreta pokemon Squirtle que herda da classe PokemonAgua."""

    def atacar(self, pokemon) -> None:
        super().atacar(pokemon)
        dano = self.ataque
        pokemon.vida -= dano
        print(f'{self} atacou com {dano} de dano!')


class Charmander(PokemonFogo):
    """Classe concreta pokemon Charmander que herda da classe PokemonFogo."""

    def atacar(self, pokemon) -> None:
        super().atacar(pokemon)
        dano = self.ataque
        pokemon.vida -= dano
        print(f'{self} atacou com {dano} de dano!')


class PokemonFactory:
    """Classe fábrica responsável pela geração de pokemons randômicos."""

    @staticmethod
    def get_pokemon() -> Pokemon:
        pokemons = [Onix(), Pikachu(), Squirtle(), Charmander()]
        return random.choice(pokemons)
