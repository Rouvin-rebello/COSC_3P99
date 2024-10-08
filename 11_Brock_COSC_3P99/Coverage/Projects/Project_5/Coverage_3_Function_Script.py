import coverage
import os
import runpy
import pytest
import sys

def measure_function_coverage(test_file_path, source_file_path):
    # Start coverage measurement
    cov = coverage.Coverage()
    cov.start()

    try:
        # Run the test file with pytest quietly
        original_stdout = sys.stdout
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            pytest.main([test_file_path, "-q"])
    except Exception as e:
        print(f"Error running test file: {e}")
    finally:
        sys.stdout = original_stdout
        cov.stop()
        cov.save()

    # Analyze coverage data
    try:
        cov.load()
        analysis = cov.analysis2(source_file_path)
        _, executable, _, missing, _ = analysis

        total_functions = len(executable)
        covered_functions = total_functions - len(missing)
        coverage_percentage = (covered_functions / total_functions) * 100

        print(f"Function Coverage: {coverage_percentage:.2f}%")
        print("Function Coverage Score:", round(coverage_percentage / 10, 2))

    except Exception as e:
        print(f"Error analyzing coverage data: {e}")

if __name__ == "__main__":
    # Define the paths to the test file and source file
    test_file_path = "test_pybubble_shooter.py"  # Replace with your actual test file path
    source_file_path = "pybubble_shooter.py"  # Replace with your actual source file path

    measure_function_coverage(test_file_path, source_file_path)
