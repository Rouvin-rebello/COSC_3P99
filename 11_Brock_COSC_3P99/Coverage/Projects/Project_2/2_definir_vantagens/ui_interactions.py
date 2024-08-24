from pokemon import Pokemon

def print_advantage_message(pokemon1: Pokemon, pokemon2: Pokemon, advantage: str):
    if advantage == 'fraqueza':
        print(f'{pokemon1} está em desvantagem na luta contra {pokemon2}')
    elif advantage == 'forca':
        print(f'{pokemon1} está em vantagem na luta contra {pokemon2}')
    else:
        print(f'Parece que o/a {pokemon1} não tem nenhuma vantagem sobre {pokemon2}')
