import traceback
import os
import sys
import coverage
import pytest  # Import pytest

def measure_function_coverage(test_file_path, source_file_path):
    # Start coverage measurement
    cov = coverage.Coverage()
    cov.start()

    original_stdout = sys.stdout  # Save the original stdout
    try:
        # Run the test file with pytest quietly
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            pytest.main([test_file_path, "-q"])
    except Exception as e:
        # Print error and traceback, ensure stdout is restored
        sys.stdout = original_stdout
        print(f"Error running test file: {e}")
        traceback.print_exc()
        cov.stop()
        cov.save()
        return
    finally:
        # Ensure stdout is restored and coverage is stopped
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
        # Print error and traceback
        print(f"Error analyzing coverage data: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    # Define the source file and test file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    sys.path.append(os.path.join(script_dir, '..', '..'))

    source_file = os.path.join(script_dir, "pacman.py")
    test_file = os.path.join(script_dir, "test_pacman.py")

    measure_function_coverage(test_file, source_file)
