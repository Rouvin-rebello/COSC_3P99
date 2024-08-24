# core_functionality.py
from ataque import (AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy)
from pokemon import Pokemon

class Batalha:
    def __init__(self, pokemon: Pokemon, pokemon2: Pokemon) -> None:
        self.participante1: Pokemon = pokemon
        self.participante2: Pokemon = pokemon2

        self.participante1.mudar_estrategia_para_luta(
            self.definir_vantagens(pokemon, self.participante2))
        self.participante2.mudar_estrategia_para_luta(
            self.definir_vantagens(pokemon2, self.participante1))

    @staticmethod
    def definir_vantagens(pokemon1: Pokemon, pokemon2: Pokemon) -> AtaqueStrategy:
        if pokemon1.fraqueza == pokemon2.tipo:
            return AtaqueComFraqueza()

        if pokemon1.forte_contra == pokemon2.tipo:
            return AtaqueComForca()

        return AtaqueNormal()

    def _restaurar_pokemons(self) -> None:
        self.participante1.recuperar_vida()
        self.participante2.recuperar_vida()

    def batalhar(self) -> str:
        while True:
            self.participante1.atacar(self.participante2)

            if self.participante2.vida <= 0:
                self._restaurar_pokemons()
                return 'Player'

            self.participante2.atacar(self.participante1)

            if self.participante1.vida <= 0:
                self._restaurar_pokemons()
                return 'Inimigo'
