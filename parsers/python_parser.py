# parsers/python_parser.py

import os
import ast


def find_python_files(project_path: str) -> list[str]:
    """
    Recursively scans a given project directory and returns a list of all Python (.py) files.
    """

    py_files = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def extract_flask_routes_from_file(file_path: str) -> list[dict]:
    """
    Parses a Python file and extracts Flask route handler functions.

    This function identifies functions decorated with `@app.route(...)`, extracts metadata
    including route path, HTTP method, function name, docstring, and the function's full source code.
    """

    with open(file_path, "r") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            return []

    routes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Check if this function has a Flask route decorator
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call) and getattr(decorator.func, 'attr', '') == 'route':
                    route_path = decorator.args[0].s if decorator.args else None
                    method = "GET"  # default
                    for kw in decorator.keywords:
                        if kw.arg == "methods":
                            if isinstance(kw.value, ast.List) and len(kw.value.elts) > 0:
                                method = kw.value.elts[0].s
                    docstring = ast.get_docstring(node)
                    function_name = node.name

                    logic = ast.get_source_segment(open(file_path).read(), node)  # crude logic string
                    routes.append({
                        "file": file_path,
                        "route": route_path,
                        "method": method,
                        "function_name": function_name,
                        "docstring": docstring,
                        "logic": logic
                    })

    return routes
