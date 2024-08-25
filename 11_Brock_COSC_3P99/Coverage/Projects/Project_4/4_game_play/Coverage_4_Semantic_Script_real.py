import coverage
from unittest import mock
import os

def extract_function_lines(source_file, function_name):
    """Extracts lines of a specified function from the source file."""
    with open(source_file, 'r') as file:
        lines = file.readlines()

    in_function = False
    function_lines = set()
    function_start = None
    function_end = None

    for i, line in enumerate(lines):
        if line.strip().startswith(f"def {function_name}("):
            in_function = True
            function_start = i

        if in_function:
            function_lines.add(i)
            if line.strip() == "":
                # Assumes function ends when encountering a blank line
                function_end = i
                break

    if function_end is None:
        function_end = len(lines)

    return function_lines, function_start, function_end

def measure_coverage(source_file, test_file, function_name):
    cov = coverage.Coverage()
    cov.start()

    try:
        exec_globals = {
            '__file__': os.path.abspath(test_file),
            'mock': mock
        }
        exec(open(test_file).read(), exec_globals)
    except Exception as e:
        print(f"Error running test file: {e}")
        cov.stop()
        cov.save()
        return 0.0

    cov.stop()
    cov.save()

    try:
        # Load and analyze the coverage data
        analysis = cov.analysis(source_file)
        
        if analysis is None:
            print("Coverage_Scripts analysis returned None.")
            return 0.0

        covered_lines = set(analysis[1]) if analysis[1] is not None else set()  # Lines covered by tests
        missed_lines = set(analysis[2]) if analysis[2] is not None else set()   # Lines not covered by tests

        # Extract lines for the specific function
        function_lines, function_start, function_end = extract_function_lines(source_file, function_name)
        
        # Identify unaccounted lines
        all_lines_in_function = set(range(function_start, function_end + 1))
        unaccounted_lines = all_lines_in_function - (covered_lines | missed_lines)
        
        # Include unaccounted lines in total statements
        total_statements = len(function_lines | unaccounted_lines)
        covered_statements = len(function_lines & covered_lines)

        # Read the source file
        with open(source_file, 'r') as file:
            lines = file.readlines()

        # Print detailed coverage information
        print("Coverage_Scripts Analysis:")
        print(f"Function lines: {function_lines}")
        print(f"Covered lines: {covered_lines}")
        print(f"Missed lines: {missed_lines}")
        print(f"Unaccounted lines: {unaccounted_lines}")

        print(f"Total Statements in Function: {total_statements}")
        
        print(f"Covered Lines ({len(function_lines & covered_lines)}):")
        for line_number in sorted(function_lines & covered_lines):
            if 0 <= line_number < len(lines):
                print(f"Line {line_number + 1}: {lines[line_number].strip()}")

        print(f"\nMissing Lines ({len(function_lines & missed_lines)}):")
        for line_number in sorted(function_lines & missed_lines):
            if 0 <= line_number < len(lines):
                print(f"Line {line_number + 1}: {lines[line_number].strip()}")

        print(f"\nUnaccounted Lines ({len(unaccounted_lines)}):")
        for line_number in sorted(unaccounted_lines):
            if 0 <= line_number < len(lines):
                print(f"Line {line_number + 1}: {lines[line_number].strip()}")

    except Exception as e:
        print(f"Error analyzing coverage data: {e}")
        return 0.0

    if total_statements == 0:
        coverage_percent = 0.0
    else:
        coverage_percent = (covered_statements / total_statements) * 100
        print(f"\nStatement Coverage_Scripts: {coverage_percent:.2f}%")
        print(f"Statement Coverage_Scripts Score: {round(coverage_percent / 10, 2)}")

    return coverage_percent

if __name__ == "__main__":
    source_file = "Function_4_UI_Interactions.py"
    test_file = "Modified_Test_File.py"

    #change the function name in the line below!!
    coverage_percent = measure_coverage(source_file, test_file, "ui_game_play")
    print(f"Statement Coverage_Scripts: {coverage_percent:.2f}%")
    print("Statement Coverage_Scripts Score:", round(coverage_percent / 10, 2))