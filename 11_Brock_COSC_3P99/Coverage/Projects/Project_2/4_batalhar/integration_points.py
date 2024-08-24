# integration_points.py
from ataque import AtaqueComForca, AtaqueComFraqueza, AtaqueNormal, AtaqueStrategy
from pokemon import Pokemon, Onix, Pikachu, Charmander, Magicarpa

def create_pokemon_instances():
    pokemon_onix = Onix(1)
    pokemon_magicarpa = Magicarpa(1)
    pokemon_pikachu = Pikachu(1)
    pokemon_charmander = Charmander(1)
    return pokemon_onix, pokemon_magicarpa, pokemon_pikachu, pokemon_charmander
