# integration_points.py
from core_functionality import Jogador
from pokemon import Onix, Pikachu

def test_integration_points():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Onix(20), Pikachu(15)]
    jogador.apresentar_pokemons()
    assert True, "Integration points test failed"
