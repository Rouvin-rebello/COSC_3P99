import coverage
import os
import runpy
import pytest
import sys

def measure_function_coverage(test_file_path, source_file_path):
    # Start coverage measurement
    cov = coverage.Coverage()
    cov.start()

    # Run the test file with pytest quietly
    try:
        # Redirect stdout to suppress pytest output
        original_stdout = sys.stdout
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            pytest.main([test_file_path, "-q"])
        sys.stdout = original_stdout
    except Exception as e:
        print(f"Error running test file: {e}")
        cov.stop()
        cov.save()
        return

    # Stop coverage measurement
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
        #print(f"Total Functions: {total_functions}")
        #print(f"Covered Functions: {covered_functions}")
        #print(f"Missing Functions: {len(missing)}")
        #print(f"Missing Function Lines: {missing}")
        print("Function Coverage Score:", round(coverage_percentage / 10, 2))

    except Exception as e:
        print(f"Error analyzing coverage data: {e}")

if __name__ == "__main__":
    # Define the paths to the test file and source file
    test_file_path = "_2_Shopping_cart_project_tests.py"  # Replace with your actual test file path
    source_file_path = "_1_Shopping_cart_project.py"  # Replace with your actual source file path

    measure_function_coverage(test_file_path, source_file_path)
