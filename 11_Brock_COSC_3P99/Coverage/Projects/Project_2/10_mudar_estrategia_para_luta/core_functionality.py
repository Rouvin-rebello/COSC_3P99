from ataque import AtaqueStrategy, AtaqueNormal

class Pokemon:
    tipo: str
    fraqueza: str
    forte_contra: str

    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel
        self.estrategia_luta: AtaqueStrategy = AtaqueNormal()

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        assert isinstance(estrategia, AtaqueStrategy), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia
