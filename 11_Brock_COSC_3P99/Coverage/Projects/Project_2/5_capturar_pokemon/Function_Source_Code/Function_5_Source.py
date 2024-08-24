from typing import List
from pokemon import Pokemon

class Pessoa:
    """ Classe abstrata """
    lista_pokemons: List[Pokemon]
    nome: str

    def capturar_pokemon(self, pokemon: Pokemon) -> None:
        """
        Método responsável por adicionar o pokemon na lista_pokemons da pessoa.

        :param pokemon: Pokemon que será adicionado a lista.
        :type pokemon: Pokemon

        :raise AssertionError: paramêtro pokemon não ser um objeto do tipo pokemon.
        :return: None
        :rtype: None
        """
        assert isinstance(pokemon, Pokemon), 'O objeto precisa ser um Pokemon'
        self.lista_pokemons.append(pokemon)
