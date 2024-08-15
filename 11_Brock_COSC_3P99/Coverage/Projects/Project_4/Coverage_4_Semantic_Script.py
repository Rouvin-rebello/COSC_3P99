import importlib.util

import coverage

def measure_coverage(source_file, test_file):
    # Initialize coverage
    cov = coverage.Coverage()

    # Start measuring coverage
    cov.start()

    # Load and run the test file as a module
    try:
        spec = importlib.util.spec_from_file_location("test_module", test_file)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
    except Exception as e:
        print(f"Error running test file: {e}")
        cov.stop()
        cov.save()
        return 0.0

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



if __name__ == "__main__":
    # Define the source file and test file
    source_file = "game.py"
    test_file = "test_game.py"

    coverage_percent = measure_coverage(source_file, test_file)
    print(f"Statement Coverage: {coverage_percent:.2f}%")
    print("Statement Coverage Score:", round(coverage_percent/10,2))



