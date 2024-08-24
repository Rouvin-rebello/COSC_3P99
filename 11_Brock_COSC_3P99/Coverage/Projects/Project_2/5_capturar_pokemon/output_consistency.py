# output_consistency.py
from core_functionality import Pessoa
from pokemon import Pokemon

def test_output_consistency():
    pessoa = Pessoa()
    pessoa.lista_pokemons = [Pokemon(), Pokemon()]
    tamanho_lista = len(pessoa.lista_pokemons)
    pessoa.capturar_pokemon(Pokemon())
    assert tamanho_lista + 1 == len(pessoa.lista_pokemons), "Output consistency test failed"
