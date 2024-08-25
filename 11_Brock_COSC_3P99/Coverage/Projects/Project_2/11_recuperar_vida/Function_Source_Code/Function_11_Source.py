from __future__ import annotations

class Pokemon:
    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel

    def recuperar_vida(self) -> None:
        """
        Método responsável por recuperar a vida do pokemon basendo
        em seu nível atual.

        :return: None
        :rtype: None
        """
        self.vida = 10 * self.nivel
