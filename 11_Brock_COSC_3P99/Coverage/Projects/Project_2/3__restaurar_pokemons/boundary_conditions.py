from pokemon import Pokemon

def verificar_vida_restaurada(pokemon1: Pokemon, pokemon2: Pokemon) -> bool:
    return pokemon1.vida == pokemon1.vida_inicial and pokemon2.vida == pokemon2.vida_inicial
