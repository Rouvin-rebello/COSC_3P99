import ast
import os
import math

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

def calculate_score(metrics):
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

    return round(max(min(base_score, 10), 1),3)


if __name__ == "__main__":
    file_path = "Function_7_Source.py"
    if os.path.exists(file_path):
        metrics = extract_test_metrics(file_path)
        score = calculate_score(metrics)
        print(f"Code Metrics Score: {score}/10")
        print("Extracted Metrics:")
        for key, value in metrics.items():
            print(f"{key}: {value}")
    else:
        print(f"File at {file_path} does not exist.")
