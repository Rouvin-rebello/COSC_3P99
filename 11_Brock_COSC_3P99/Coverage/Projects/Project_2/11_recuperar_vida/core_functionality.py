class Pokemon:
    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel

    def recuperar_vida(self) -> None:
        self.vida = 10 * self.nivel
