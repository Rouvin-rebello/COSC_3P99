import coverage
import unittest
from pokemon import Pokemon


def measure_coverage(source_file, test_file):
    # Initialize coverage
    cov = coverage.Coverage()

    # Start measuring coverage
    cov.start()

    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern=test_file)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Stop measuring coverage
    cov.stop()
    cov.save()

    # Analyze the coverage data
    total_statements = 0
    covered_statements = 0

    try:
        analysis = cov.analysis(source_file)
        total_statements = len(analysis[1]) + len(analysis[2])
        covered_statements = len(analysis[1])
    except Exception as e:
        print(f"Error analyzing coverage data: {e}")
        return 0.0

    # Calculate statement coverage
    if total_statements == 0:
        coverage_percent = 0.0
    else:
        coverage_percent = (covered_statements / total_statements) * 100

    return coverage_percent


class Batalha:
    def __init__(self, pokemon: Pokemon, pokemon2: Pokemon) -> None:
        if not isinstance(pokemon, Pokemon) or not isinstance(pokemon2, Pokemon):
            raise ValueError("Os participantes devem ser instâncias da classe Pokemon")
        self.participante1: Pokemon = pokemon
        self.participante2: Pokemon = pokemon2



if __name__ == "__main__":
    # Define the source file and test file
    source_file = "core_functionality.py"
    test_file = "Modified_Test_File.py"

    coverage_percent = measure_coverage(source_file, test_file)
    print(f"Statement Coverage_Scripts: {coverage_percent:.2f}%")
    print("Statement Coverage_Scripts Score:", round(coverage_percent / 10, 2))
