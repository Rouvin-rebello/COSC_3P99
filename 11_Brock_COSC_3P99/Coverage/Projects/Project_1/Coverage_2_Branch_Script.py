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


if __name__ == "__main__":
    # Define the source file and test file
    source_file = "_1_Shopping_cart_project.py"  # Replace with your source file name
    test_file = "_2_Shopping_cart_project_tests.py"  # Replace with your test file name

    branch_coverage_percent = measure_branch_coverage(source_file, test_file)
    print(f"Branch Coverage: {branch_coverage_percent:.2f}%")
    print("Branch Coverage Score:", round(branch_coverage_percent / 10, 2))