from pokemon import Pokemon

class Batalha:
    """
    Classe responsável por organizar e realizar a batalha
    entre dois pokemons diferentes.

    Atributos:
        participante1 (Pokemon): Pokemon do jogador que vai batalhar.
        participante2 (Pokemon): Pokemon do inimigo que o jogador vai batalhar
    """

    def __init__(self, pokemon: Pokemon, pokemon2: Pokemon) -> None:
        self.participante1: Pokemon = pokemon
        self.participante2: Pokemon = pokemon2

    def _restaurar_pokemons(self) -> None:
        """ Método privado para a recuperação da vida dos pokemons pós luta."""
        self.participante1.recuperar_vida()
        self.participante2.recuperar_vida()
