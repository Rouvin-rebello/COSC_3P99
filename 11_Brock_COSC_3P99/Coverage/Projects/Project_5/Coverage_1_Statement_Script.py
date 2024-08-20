import os
import coverage
import mock  # Assuming 'mock' is needed for your test file

def measure_coverage(source_file, test_file):
    # Initialize coverage
    cov = coverage.Coverage()

    # Start measuring coverage
    cov.start()

    # Run the test file
    try:
        exec_globals = {
            '__file__': os.path.abspath(test_file),
            'mock': mock
        }
        with open(test_file) as f:
            code = f.read()
        exec(code, exec_globals)
    except Exception as e:
        print(f"Error running test file: {e}")
        cov.stop()
        cov.save()
        return 0.0

    # Stop measuring coverage
    cov.stop()
    cov.save()

    # Analyze the coverage data
    total_statements = set()
    covered_statements = set()
    uncovered_statements = set()

    try:
        analysis = cov.analysis(source_file)
        covered_statements.update(analysis[1])
        uncovered_statements.update(analysis[2])
        total_statements.update(analysis[1])
        total_statements.update(analysis[2])
    except Exception as e:
        print(f"Error analyzing coverage data: {e}")
        return 0.0

    # Map line numbers to code lines
    with open(source_file, 'r') as f:
        source_lines = f.readlines()

    # Print covered statements
    print("\nCovered Statements:")
    for line_num in sorted(covered_statements):
        print(f"Line {line_num}: {source_lines[line_num - 1].strip()}")

    # Print uncovered statements
    print("\nUncovered Statements:")
    for line_num in sorted(uncovered_statements):
        print(f"Line {line_num}: {source_lines[line_num - 1].strip()}")

    # Calculate statement coverage
    if len(total_statements) == 0:
        coverage_percent = 0.0
    else:
        coverage_percent = (len(covered_statements) / len(total_statements)) * 100
        print(f"\nTotal unique statements: {len(total_statements)}")
        print(f"Covered unique statements: {len(covered_statements)}")

    return coverage_percent


if __name__ == "__main__":
    # Define the source file and test file
    source_file = "Function_split.py"
    test_file = "test_pybubble_shooter.py"

    coverage_percent = measure_coverage(source_file, test_file)
    print(f"\nStatement Coverage: {coverage_percent:.2f}%")
    print("Statement Coverage Score:", round(coverage_percent/10, 2))
