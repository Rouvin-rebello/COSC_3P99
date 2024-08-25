class Pokemon:
    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel

    def subir_nivel(self) -> None:
        """
        Método responsável por subir 2 níveis do pokemon e reconfigurar-lo.
        :return: None
        :rtype: None
        """
        self.nivel += 2
        self._reconfigurar_status()

    def _reconfigurar_status(self) -> None:
        """
        Método privado responsável por reconfigurar os atributos
        baseando-se no novo nível do pokemon.
        :return: None
        :rtype: None
        """
        self.vida = 10 * self.nivel
        self.ataque_base = 4 * self.nivel
