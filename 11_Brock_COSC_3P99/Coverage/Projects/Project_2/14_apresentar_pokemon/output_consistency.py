import logging
from core_functionality import Pokemon

logging.basicConfig(level=logging.INFO)

class PresentPokemon(Pokemon):
    def apresentar_pokemon(self) -> None:
        """
        Método responsável por mostrar todas as informações do pokemon.
        """
        logging.info(f'pokemon: {self.__class__.__name__}')
        logging.info(f'Level: {self.nivel}')
        logging.info(f'Vida: {self.vida} de pontos.')
        logging.info(f'Dano base: {self.ataque_base}')
