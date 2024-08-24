
from core_functionality import Jogador
from pokemon import Pokemon

def test_ui_interactions():
    jogador = Jogador('walex')
    jogador.lista_pokemons = [Pokemon(20)]

    jogador._resultado_da_batalha('Player', 0)
    jogador._resultado_da_batalha('Inimigo', 0)
