import coverage
import runpy


def measure_branch_coverage(source_file, test_file):
    # Initialize coverage with branch tracking enabled
    cov = coverage.Coverage(branch=True)

    # Start measuring coverage
    cov.start()

    # Run the test file
    try:
        runpy.run_path(test_file)
    except Exception as e:
        print(f"Error running test file: {e}")
        cov.stop()
        cov.save()
        return 0.0

    # Stop measuring coverage
    cov.stop()
    cov.save()

    # Analyze the coverage data
    try:
        analysis = cov.analysis2(source_file)
        missing_branches = analysis[3]
        executed_branches = analysis[4]
    except Exception as e:
        print(f"Error analyzing coverage data: {e}")
        return 0.0

    # Calculate branch coverage
    total_branches = len(missing_branches) + len(executed_branches)

    if total_branches == 0:
        coverage_percent = 0.0
    else:
        coverage_percent = (len(executed_branches) / total_branches) * 100

    return coverage_percent


file = 15


if __name__ == "__main__":
    # Define the source file and test file
    source_file = "Function_" + str(file) + "_Source.py"
    test_file = "Function_" + str(file) + "_Test.py"

    branch_coverage_percent = measure_branch_coverage(source_file, test_file)
    print(f"Branch Coverage_Scripts: {branch_coverage_percent:.2f}%")
    print("Branch Coverage_Scripts Score:", round(branch_coverage_percent / 10, 2))