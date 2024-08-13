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

    # Map line numbers to code lines
    with open(source_file, 'r') as f:
        source_lines = f.readlines()

    def print_branch_info(branches, branch_type):
        print(f"\n{branch_type} Branches:")
        for branch in branches:
            try:
                if isinstance(branch, tuple):
                    line_num, branch_id = branch
                    print(f"Line {line_num} (Branch ID {branch_id}): {source_lines[int(line_num) - 1].strip()}")
                else:
                    line_num = int(branch)
                    print(f"Line {line_num}: {source_lines[line_num - 1].strip()}")
            except ValueError:
                print(f"Skipping invalid branch data: {branch}")

    # Print executed and missing branches
    print_branch_info(executed_branches, "Executed")
    print_branch_info(missing_branches, "Missing")

    # Calculate branch coverage
    total_branches = len(missing_branches) + len(executed_branches)

    if total_branches == 0:
        coverage_percent = 0.0
    else:
        coverage_percent = (len(executed_branches) / total_branches) * 100

    return coverage_percent


if __name__ == "__main__":
    # Define the source file and test file
    source_file = "Function_split.py"
    test_file = "test_pybubble_shooter.py"

    branch_coverage_percent = measure_branch_coverage(source_file, test_file)
    print(f"\nBranch Coverage: {branch_coverage_percent:.2f}%")
    print("Branch Coverage Score:", round(branch_coverage_percent / 10, 2))
