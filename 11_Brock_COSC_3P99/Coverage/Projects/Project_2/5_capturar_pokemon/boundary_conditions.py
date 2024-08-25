# boundary_conditions.py
from core_functionality import Pessoa
from pokemon import Pokemon

def test_boundary_conditions():
    pessoa = Pessoa()
    pessoa.lista_pokemons = [Pokemon(), Pokemon()]

    try:
        pessoa.capturar_pokemon('pokemon')
    except AssertionError as e:
        print(e)  # Expected: 'O objeto precisa ser um Pokemon'

