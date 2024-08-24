from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy
from pokemon import Pokemon

def get_attack_strategy(pokemon1: Pokemon, pokemon2: Pokemon) -> AtaqueStrategy:
    if pokemon1.fraqueza == pokemon2.tipo:
        return AtaqueComFraqueza()

    if pokemon1.forte_contra == pokemon2.tipo:
        return AtaqueComForca()

    return AtaqueNormal()
