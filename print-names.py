import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("No name provided. Usage: python print-names.py <name>")
