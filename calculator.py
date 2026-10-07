import sys

def calculate(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError(f"Unknown operator: {op}")

if __name__ == "__main__":
    try:
        a, op, b = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
        print(calculate(a, op, b))
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

