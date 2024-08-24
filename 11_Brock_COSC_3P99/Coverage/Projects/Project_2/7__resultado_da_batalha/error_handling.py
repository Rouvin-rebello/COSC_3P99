# error_handling.py
from core_functionality import Jogador
from pokemon import Pokemon

def test_error_handling():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Pokemon(20)]

    try:
        jogador._resultado_da_batalha('Invalid', 0)
    except Exception as e:
        print(f"Handled error: {e}")
