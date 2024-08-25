# error_handling.py
from core_functionality import Pessoa
from pokemon import Pokemon

def test_error_handling():
    pessoa = Pessoa()
    pessoa.lista_pokemons = [Pokemon(), Pokemon()]

    try:
        pessoa.capturar_pokemon('pokemon')
    except AssertionError as e:
        print(f"Handled error: {e}")  # Expected: 'O objeto precisa ser um Pokemon'
