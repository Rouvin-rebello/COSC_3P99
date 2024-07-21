import subprocess
import time
import sys


def measure_test_execution_time(test_file_path):
    start_time = time.time()

    # Run the pytest on the provided test file path
    result = subprocess.run([sys.executable, '-m', 'pytest', test_file_path], capture_output=True, text=True)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, result.stdout, result.stderr


def count_lines_of_code(test_file_path):
    with open(test_file_path, 'r') as file:
        lines = file.readlines()
        # Count non-empty, non-comment lines
        loc = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
    return loc


def score_execution_time(execution_time, loc):
    # Adjusting the score based on both execution time and LOC
    if execution_time <= 0.5:
        if loc <= 50:
            return 10
        elif loc <= 100:
            return 9
        else:
            return 8
    elif execution_time <= 1:
        if loc <= 50:
            return 8
        elif loc <= 100:
            return 7
        else:
            return 6
    elif execution_time <= 1.5:
        if loc <= 50:
            return 7
        elif loc <= 100:
            return 6
        else:
            return 5
    elif execution_time <= 2:
        if loc <= 50:
            return 6
        elif loc <= 100:
            return 5
        else:
            return 4
    elif execution_time <= 2.5:
        if loc <= 50:
            return 5
        elif loc <= 100:
            return 4
        else:
            return 3
    elif execution_time <= 3:
        if loc <= 50:
            return 4
        elif loc <= 100:
            return 3
        else:
            return 2
    elif execution_time <= 3.5:
        if loc <= 50:
            return 3
        elif loc <= 100:
            return 2
        else:
            return 1
    else:
        return 1


if __name__ == "__main__":
    # Specify the test file path here
    test_file_path = "Shopping_cart_project_tests.py"

    execution_time, stdout, stderr = measure_test_execution_time(test_file_path)
    loc = count_lines_of_code(test_file_path)
    score = score_execution_time(execution_time, loc)

    print(f"Test Execution Time: {execution_time:.2f} seconds")
    print(f"Lines of Code: {loc}")
    print(f"Performance Score: {score}/10")
    print("\nTest Output:\n")
    print(stdout)
    if stderr:
        print("\nTest Errors:\n")
        print(stderr)
