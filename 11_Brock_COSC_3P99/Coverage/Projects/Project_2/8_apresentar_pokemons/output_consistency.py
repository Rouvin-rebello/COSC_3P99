# output_consistency.py
from core_functionality import Jogador
from pokemon import Onix, Pikachu

def test_output_consistency():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Onix(20), Pikachu(15)]

    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    jogador.apresentar_pokemons()
    sys.stdout = sys.__stdout__

    expected_output = (
        "Digite = 0 para escolher o/a Onix de nível 20 e dano base de 80\n"
        "Digite = 1 para escolher o/a Pikachu de nível 15 e dano base de 60\n"
    )
    assert captured_output.getvalue() == expected_output, "Output consistency test failed"
