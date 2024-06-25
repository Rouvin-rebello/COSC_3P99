import re


def calculate_score(occurrences):
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

    with open(file_path, 'r') as file:
        content = file.read()

    for smell, pattern in smells.items():
        matches = re.findall(pattern, content)
        if matches:
            score = calculate_score(len(matches))
            final_score += score
            results[smell] = {
                'score': score,
                'occurrences': matches
            }

    return final_score, results


if __name__ == '__main__':
    file_path = 'Shopping_cart_project_tests.py'  # Replace with the path to your Python file
    final_score, found_smells = check_code_smells(file_path)

    if found_smells:
        print("Code smells found:")
        for smell, info in found_smells.items():
            score = info['score']
            occurrences = len(info['occurrences'])
            print(f"{smell}: Score {score}/10, {occurrences} occurrences")
            # Optionally, print out the occurrences if needed:
            # for occurrence in occurrences:
            #     print(f"   {occurrence}")
        print(f"\nFinal Aggregated Score: {final_score/10}/10")
    else:
        print("No code smells found.")
