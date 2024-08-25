try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise


import ast
import os
import math
import re
import subprocess
import time
import sys


class TestMetricsExtractor(ast.NodeVisitor):
    def __init__(self):
        self.metrics = {
            "ALU": False,
            "NOAIT": 0,
            "NOASIT": 0,
            "NOAU": 0,
            "NOBU": 0,
            "NOCT": 0,
            "NODT": 0,
            "NODV": 0,
            "NOECU": False,
            "NOEET": 0,
            "NOET": 0,
            "NOFS": 0,
            "NOIS": 0,
            "NONO": 0,
            "NOPT": 0,
            "NORT": 0,
            "NOST": 0
        }

    def visit_FunctionDef(self, node):
        if node.name.startswith('test_'):
            self.metrics["NOCT"] += 1
            for stmt in node.body:
                if isinstance(stmt, ast.Assert):
                    self.metrics["NOAIT"] += 1
                if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                    if isinstance(stmt.value.func, ast.Name) and stmt.value.func.id == 'assume':
                        self.metrics["NOASIT"] += 1
                if isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Name):
                    if stmt.func.id == 'ErrorCollector':
                        self.metrics["NOECU"] = True
                if isinstance(stmt, ast.If):
                    self.metrics["NOIS"] += 1
                if isinstance(stmt, ast.For):
                    self.metrics["NOFS"] += 1
                if isinstance(stmt, ast.Call) and isinstance(stmt.func, ast.Name):
                    if stmt.func.id in ('Hamcrest', 'Assertj', 'Atrium', 'Truth', 'Valid4j', 'Datasource-Assert'):
                        self.metrics["ALU"] = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module in ('Hamcrest', 'Assertj', 'Atrium', 'Truth', 'Valid4j', 'Datasource-Assert'):
            self.metrics["ALU"] = True
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.metrics["NODV"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'new':
            self.metrics["NONO"] += 1
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == 'dynamicTest':
                self.metrics["NODT"] += 1
            elif node.func.attr == 'parameterizedTest':
                self.metrics["NOPT"] += 1
            elif node.func.attr == 'repeatedTest':
                self.metrics["NORT"] += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        if any(isinstance(handler.type, ast.Name) and handler.type.id == 'Exception' for handler in node.handlers):
            self.metrics["NOEET"] += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if any(base.id == 'Test' for base in node.bases):
            self.metrics["NOET"] += 1
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef) and stmt.name.startswith('test_'):
                self.metrics["NOST"] += 1
        self.generic_visit(node)

    def visit_Decorator(self, node):
        if isinstance(node, ast.Name):
            if node.id == 'before':
                self.metrics["NOBU"] += 1
            if node.id == 'after':
                self.metrics["NOAU"] += 1
        self.generic_visit(node)


def extract_test_metrics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)
    extractor = TestMetricsExtractor()
    extractor.visit(tree)
    return extractor.metrics


def calculate_metrics_score(metrics):
    issues_weight = {
        "NOAIT": 1,
        "NOASIT": 1,
        "NOAU": 0.5,
        "NOBU": 0.5,
        "NOCT": 2,
        "NODT": 1,
        "NODV": 1,
        "NOEET": 1,
        "NOET": 1,
        "NOFS": 1,
        "NOIS": 1,
        "NONO": 1,
        "NOPT": 1,
        "NORT": 1,
        "NOST": 1,
    }

    base_score = 10
    for key, weight in issues_weight.items():
        base_score -= metrics[key] * weight * 0.1

    if not metrics["ALU"]:
        base_score -= 1
    if metrics["NOECU"]:
        base_score -= 1

    return round(max(min(base_score, 10), 1), 3)


def calculate_code_smell_score(occurrences):
    if occurrences <= 1:
        return 1
    elif occurrences <= 3:
        return 2
    elif occurrences <= 5:
        return 3
    elif occurrences <= 7:
        return 4
    elif occurrences <= 10:
        return 5
    elif occurrences <= 15:
        return 6
    elif occurrences <= 20:
        return 7
    elif occurrences <= 30:
        return 8
    elif occurrences <= 50:
        return 9
    else:
        return 10


def check_code_smells(file_path):
    smells = {
        'LC': r'class\s+\w+\s*:',
        'LPL': r'def\s+\w+\((?:\s*\w+\s*(?:,|\)))*:',
        'LM': r'def\s+\w+\s*\((?:.|\n)*?\):',
        'LMC': r'\.\w+' * 3,
        'LSC': r'(?:\.\w+)*',
        'LBCL': r'(\w+)*',
        'UEH': r'except\s*:',
        'LLF': r'lambda\s+\w+\s*:',
        'CLC': r'[\[\]]',
        'LEC': r'(\.\w+)*',
        'LTCE': r'\?\w+',
        'Assertion roulette': r'assert\s*:',
        'Lazy Test': r'(if)\s*',
        'Magic Number': r'\d',
        'Redundant Print': r'print\(\w+\)'
    }

    final_score = 0
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for smell, pattern in smells.items():
        matches = re.findall(pattern, content)
        if matches:
            score = calculate_code_smell_score(len(matches))
            final_score += score
            results[smell] = {
                'score': score,
                'occurrences': matches
            }

    return final_score, results


def run_pylint(file_path):
    try:
        pylint_path = 'C:/Users/Rouvin/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/Scripts/pylint.exe'

        if not os.path.isfile(file_path) or not file_path.endswith('.py'):
            print(f'Invalid file path: {file_path}')
            return None

        result = subprocess.run([pylint_path, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        score_match = re.search(r'Your code has been rated at (-?\d+\.\d+)/10', result.stdout)

        if score_match:
            score = float(score_match.group(1))
            print(f'Static Analysis score: {score}/10')
            return score
        else:
            print(f'Could not determine pylint score for {file_path}.')
            #print(result.stdout)
            return None
    except FileNotFoundError:
        print(f'Pylint executable not found. Please ensure pylint is installed and in your PATH.')
    except Exception as e:
        print(f'An error occurred while running pylint: {e}')
        return None


def measure_test_execution_time(test_file_path):
    start_time = time.time()

    result = subprocess.run([sys.executable, '-m', 'pytest', test_file_path], capture_output=True, text=True)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, result.stdout, result.stderr


def count_lines_of_code(test_file_path):
    with open(test_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        loc = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
    return loc


def score_execution_time(execution_time, loc):
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


file = 6

if __name__ == "__main__":
    # File paths
    source_file_path = "Function_" + str(file) + "_Source.py"
    test_file_path = "Function_" + str(file) + "_Test.py"

    # Metrics extraction
    if os.path.exists(source_file_path):
        metrics = extract_test_metrics(source_file_path)
        metrics_score = calculate_metrics_score(metrics)
        print(f"Code Metrics Score: {metrics_score}/10")
        #print("Extracted Metrics:")
        #for key, value in metrics.items():
        #    print(f"{key}: {value}")
    else:
        print(f"File at {source_file_path} does not exist.")

    # Code smells check
    if os.path.exists(source_file_path):
        final_smell_score, found_smells = check_code_smells(source_file_path)
        if found_smells:
            #print("Code smells found:")
            for smell, info in found_smells.items():
                score = info['score']
                occurrences = len(info['occurrences'])
                #print(f"{smell}: Score {score}/10, {occurrences} occurrences")
            print(f"Code Smells Score: {final_smell_score/10}/10")
        else:
            print("No code smells found.")
    else:
        print(f"File at {source_file_path} does not exist.")

    # Pylint run
    if os.path.exists(source_file_path):
        pylint_score = run_pylint(source_file_path)
    else:
        print(f"File at {source_file_path} does not exist.")

    # Test execution and performance score
    if os.path.exists(test_file_path):
        execution_time, stdout, stderr = measure_test_execution_time(test_file_path)
        loc = count_lines_of_code(test_file_path)
        performance_score = score_execution_time(execution_time, loc)

        #print(f"Test Execution Time: {execution_time:.2f} seconds")
        #print(f"Lines of Code: {loc}")
        print(f"Test Execution Score: {performance_score}/10")
        #print("\nTest Output:\n")
        #print(stdout)
        if stderr:
            print("\nTest Errors:\n")
            print(stderr)
    else:
        print(f"Test file at {test_file_path} does not exist.")
