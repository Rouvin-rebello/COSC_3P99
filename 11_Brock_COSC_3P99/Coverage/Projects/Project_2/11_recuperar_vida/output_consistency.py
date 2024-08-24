from core_functionality import Pokemon

def test_output_consistency():
    # Ensure `recuperar_vida` consistently resets `vida` to the correct value
    pokemon = Pokemon(nivel=5)
    initial_vida = pokemon.vida
    pokemon.vida -= 20
    pokemon.recuperar_vida()
    assert pokemon.vida == initial_vida, "Output consistency failed: vida should be restored to the initial value"

