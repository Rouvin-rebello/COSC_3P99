# error_handling.py
from core_functionality import Jogador

def test_error_handling():
    jogador = Jogador('walex')
    try:
        jogador.apresentar_pokemons()
    except Exception as e:
        print(f"Handled error: {e}")
