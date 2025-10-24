def calculate(expression: str):
    try:
        exp = expression.replace("calculate", "").strip()
        result = eval(exp)
        return f"The answer is {result}"
    except Exception as e:
        return "Sorry, I couldn’t calculate that."
