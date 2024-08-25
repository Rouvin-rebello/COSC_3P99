from core_functionality import Pokemon

def test_boundary_conditions():
    # Example of a boundary condition: setting `vida` to a negative value
    pokemon = Pokemon(nivel=5)
    pokemon.vida = -20
    pokemon.recuperar_vida()
    assert pokemon.vida == 50, "Boundary condition failed: vida should be reset to 50"
