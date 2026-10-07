import sys
import math

import math

def _sqrt(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def _inv(a):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    return 1 / a

def _log(a):
    if a <= 0:
        raise ValueError("Log needs a positive number")
    return math.log10(a)

def _ln(a):
    if a <= 0:
        raise ValueError("Ln needs a positive number")
    return math.log(a)

def _tan(a):
    if round(math.cos(math.radians(a)), 10) == 0:
        raise ValueError("Tan is undefined here")
    return round(math.tan(math.radians(a)), 10)

UNARY = {
    "sqrt": _sqrt,
    "sq": lambda a: a * a,
    "inv": _inv,
    "log": _log,
    "ln": _ln,
    "sin": lambda a: round(math.sin(math.radians(a)), 10),
    "cos": lambda a: round(math.cos(math.radians(a)), 10),
    "tan": _tan,
}
def calculate(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "%": return a % b
    if op == "**": return a ** b
    if op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    if op in UNARY: return UNARY[op](a)
    raise ValueError(f"Unknown operator: {op}")

if __name__ == "__main__":
    try:
        a, op, b = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
        print(calculate(a, op, b))
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

