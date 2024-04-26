import ast
import subprocess

def install_packages_from_file(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())

    packages = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                packages.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            packages.add(node.module)

    for package in packages:
        subprocess.run(['pip', 'install', package])

if __name__ == "__main__":
    python_file = input("Enter the Python file name: ")
    install_packages_from_file(python_file)
