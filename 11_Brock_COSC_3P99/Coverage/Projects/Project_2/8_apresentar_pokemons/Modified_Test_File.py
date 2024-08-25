try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise


# test_all.py
import unittest
from core_functionality import Jogador
from pokemon import Onix, Pikachu
from boundary_conditions import test_boundary_conditions
from error_handling import test_error_handling
from integration_points import test_integration_points
from ui_interactions import test_ui_interactions
from output_consistency import test_output_consistency

class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Onix(20), Pikachu(15)]

    def test_apresentar_pokemons_mostra_os_pokemons_corretamente(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.jogador.apresentar_pokemons()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Digite = 0 para escolher o/a Onix de nível 20 e dano base de 80\n"
            "Digite = 1 para escolher o/a Pikachu de nível 15 e dano base de 60\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_boundary_conditions(self):
        test_boundary_conditions()

    def test_error_handling(self):
        test_error_handling()

    def test_integration_points(self):
        test_integration_points()

    def test_ui_interactions(self):
        test_ui_interactions()

    def test_output_consistency(self):
        test_output_consistency()

if __name__ == '__main__':
    unittest.main()
