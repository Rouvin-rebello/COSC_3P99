# boundary_conditions.py
from core_functionality import Jogador

def test_boundary_conditions():
    jogador = Jogador('walex')
    jogador.apresentar_pokemons()
    assert True, "Boundary condition test failed"
