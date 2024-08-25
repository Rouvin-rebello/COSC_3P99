from core_functionality import Pokemon, AtaqueStrategy

class PokemonErrorHandling(Pokemon):
    def atacar(self, pokemon: Pokemon) -> None:
        assert isinstance(pokemon, Pokemon), 'Objeto precisa ser do tipo Pokemon'

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        assert isinstance(estrategia, AtaqueStrategy), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia
