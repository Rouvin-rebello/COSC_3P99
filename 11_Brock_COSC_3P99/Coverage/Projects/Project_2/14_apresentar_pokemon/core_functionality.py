class Pokemon:
    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel
