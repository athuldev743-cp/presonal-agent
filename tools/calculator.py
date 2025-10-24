# calculator.py
import ast
import operator

# Allowed operations
allowed_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def safe_eval(expr):
    """Safely evaluate a math expression."""
    try:
        node = ast.parse(expr, mode='eval').body

        def _eval(n):
            if isinstance(n, ast.Num):
                return n.n
            elif isinstance(n, ast.BinOp):
                if type(n.op) in allowed_ops:
                    return allowed_ops[type(n.op)](_eval(n.left), _eval(n.right))
                else:
                    raise ValueError("Operation not allowed")
            elif isinstance(n, ast.UnaryOp):
                if type(n.op) in allowed_ops:
                    return allowed_ops[type(n.op)](_eval(n.operand))
                else:
                    raise ValueError("Operation not allowed")
            else:
                raise ValueError("Expression not allowed")
        return _eval(node)
    except Exception:
        raise ValueError("Invalid expression")

def calculate(expression: str):
    try:
        exp = expression.lower().replace("calculate", "").strip()
        # Optional safety — only allow numbers and math ops
        allowed_chars = "0123456789+-*/.%() "
        if not all(c in allowed_chars for c in exp):
            return "Sorry, that looks unsafe to calculate."
        result = eval(exp)
        return f"The answer is {result}"
    except Exception:
        return "Sorry, I couldn’t calculate that."
