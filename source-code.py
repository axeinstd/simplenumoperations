class NotMathsExpression(Exception):
    pass


def is_expr(expression: str) -> bool:
    can_expr = ['+', '-', '/', '*', '%', '**', ' ']
    for i in can_expr:
        expression = expression.replace(i, '')
    if not expression.isdigit():
        return False
    return True


def calculate(expression):
    if is_expr(expression) is False:
        raise NotMathsExpression('Input data is not expression!')
    return eval(expression)
