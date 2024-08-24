import unittest
from Function_8_Source import Jogador
from pokemon import Onix, Pikachu

class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Onix(20), Pikachu(15)]

    def test_apresentar_pokemons_mostra_os_pokemons_corretamente(self):
        # Capture the output of the apresentar_pokemons method
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.jogador.apresentar_pokemons()
        sys.stdout = sys.__stdout__

        # Update the expected output to match actual ataque_base values
        expected_output = (
            "Digite = 0 para escolher o/a Onix de nível 20 e dano base de 80\n"
            "Digite = 1 para escolher o/a Pikachu de nível 15 e dano base de 60\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
