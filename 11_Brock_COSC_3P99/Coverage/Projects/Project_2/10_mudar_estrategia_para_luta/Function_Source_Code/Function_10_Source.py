from __future__ import annotations

try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'src'
            )
        )
    )
except:
    raise

from ataque import AtaqueStrategy, AtaqueNormal

class Pokemon:
    """
    Classe abstrata pokemon responsável por configurar o comportamento
    genérico de todos os pokemons.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.
    """
    tipo: str
    fraqueza: str
    forte_contra: str

    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel
        self.estrategia_luta: AtaqueStrategy = AtaqueNormal()

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        """
        Método responsável por mudar a estrategia de ataque de acordo
        com o oponente que irá enfrentar.

        :param estrategia: Estrategia que será adicionada ao pokemon.
        :type estrategia: AtaqueStrategy

        :raise AssertionError: Parâmetro não é um objeto AtaqueStrategy.

        :return: None
        :rtype: None
        """
        assert isinstance(
            estrategia,
            AtaqueStrategy
        ), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia
