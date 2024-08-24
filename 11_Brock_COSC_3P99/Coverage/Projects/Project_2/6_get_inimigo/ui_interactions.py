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

ui_interactions.py
from core_functionality import Jogador
from pokemon import Pokemon

def test_ui_interactions():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Pokemon(20)]

    jogador._resultado_da_batalha('Player', 0)
    jogador._resultado_da_batalha('Inimigo', 0)
