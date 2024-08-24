import subprocess
import re
import os


def run_pylint(file_path):
    try:
        # Full path to pylint executable
        pylint_path = 'C:/Users/Rouvin/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/Scripts/pylint.exe'

        # Ensure the file_path is a Python file
        if not os.path.isfile(file_path) or not file_path.endswith('.py'):
            print(f'Invalid file path: {file_path}')
            return None

        # Run pylint on the given file and capture the output
        result = subprocess.run([pylint_path, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Extract the score from pylint output
        score_match = re.search(r'Your code has been rated at (-?\d+\.\d+)/10', result.stdout)

        if score_match:
            score = float(score_match.group(1))
            print(f'Pylint score for {file_path}: {score}/10')
            return score
        else:
            print(f'Could not determine pylint score for {file_path}.')
            print(result.stdout)
            return None
    except FileNotFoundError:
        print(f'Pylint executable not found. Please ensure pylint is installed and in your PATH.')
    except Exception as e:
        print(f'An error occurred while running pylint: {e}')
        return None


# Replace 'path/to/your/file.py' with the actual path to your file
file_path = "Function_7_Source.py"
run_pylint(file_path)
