try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise

# output_consistency.py
from core_functionality import Jogador
from pokemon import Pokemon

def test_output_consistency():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Pokemon(20)]

    nivel_pokemon_que_lutou_antes_da_luta = jogador.lista_pokemons[0].nivel
    jogador._resultado_da_batalha('Player', 0)
    assert jogador.lista_pokemons[0].nivel == nivel_pokemon_que_lutou_antes_da_luta + 2, "Output consistency test failed"
