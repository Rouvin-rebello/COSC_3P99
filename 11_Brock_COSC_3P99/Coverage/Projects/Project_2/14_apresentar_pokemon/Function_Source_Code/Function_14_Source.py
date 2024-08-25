import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)

class Pokemon:
    # ... other methods and attributes ...

    def apresentar_pokemon(self) -> None:
        """
        Método responsável por mostrar todas as informações do pokemon.
        """
        logging.info(f'pokemon: {self.__class__.__name__}')
        logging.info(f'Level: {self.nivel}')
        logging.info(f'Vida: {self.vida} de pontos.')
        logging.info(f'Dano base: {self.ataque_base}')
