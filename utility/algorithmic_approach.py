import ast


class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.complexity = "O(1)"
        self.recursive_funcs = set()

    def visit_FunctionDef(self, node):
        if self._is_recursive(node):
            self.recursive_funcs.add(node.name)
        self.generic_visit(node)

    def visit_For(self, node):
        if self._is_iterating_variable(node.iter):
            self.complexity = self._increase_complexity(self.complexity, "n")
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity = self._increase_complexity(self.complexity, "n")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.recursive_funcs:
            self.complexity = self._increase_complexity(self.complexity, "n^r")
        self.generic_visit(node)

    def _is_recursive(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                if child.func.id == node.name:
                    return True
        return False

    def _is_iterating_variable(self, iter_node):
        if isinstance(iter_node, ast.Call) and isinstance(iter_node.func, ast.Name):
            if iter_node.func.id == "range":
                return True
        return False

    def _increase_complexity(self, current_complexity, new_factor):
        if "r" in new_factor:  # recursion detected
            return "O(n^r)"
        elif current_complexity == "O(1)":
            return f"O({new_factor})"
        elif current_complexity == f"O({new_factor})":
            return f"O({new_factor}^2)"
        else:
            return f"O({new_factor} * {current_complexity[2:]})"


def analyze_complexity(code):
    try:
        tree = ast.parse(code)
        analyzer = ComplexityAnalyzer()
        analyzer.visit(tree)
        return analyzer.complexity
    except SyntaxError:
        return "Invalid Python code"


# Example usage
code = """
def example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

def recursive_example(n):
    if n <= 1:
        return 1
    else:
        return recursive_example(n-1) + recursive_example(n-1)
"""

print(analyze_complexity(code))  # Output: O(n^r)
