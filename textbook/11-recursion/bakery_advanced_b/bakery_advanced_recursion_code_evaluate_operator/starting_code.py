from cisc108 import assert_equal
from dataclasses import dataclass

@dataclass
class Expression:
    pass

@dataclass
class BinaryExpression(Expression):
    operator: str
    left: Expression
    right: Expression
    
@dataclass
class IntegerExpression(Expression):
    value: int

###### Edit below #################################################################
    
def evaluate_math(expression: Expression) -> int:
    if isinstance(expression, IntegerExpression):
        # In this base case, you *know* that expression is an IntegerExpression!
        return ___
    # In this recursive case, you *know* that expression is a BinaryExpression!
    # ...
    # ... Replace these comments with the real code!
    # ...
    return ___

# 5 + 3
assert_equal(evaluate_math(BinaryExpression("+", IntegerExpression(5), IntegerExpression(3))), 8)
# 3 * 4
assert_equal(evaluate_math(BinaryExpression("*", IntegerExpression(3), IntegerExpression(4))), 12)
# (2 * 5) + (5 * 3)
assert_equal(evaluate_math(BinaryExpression("+",
                                            BinaryExpression("*", IntegerExpression(2), IntegerExpression(5)),
                                            BinaryExpression("*", IntegerExpression(5), IntegerExpression(3)))), 25)
# (5 * (5 + 5)) * 3
assert_equal(evaluate_math(BinaryExpression("*",
                                            BinaryExpression("*",
                                                             BinaryExpression("+", IntegerExpression(5), IntegerExpression(5)),
                                                             IntegerExpression(5)),
                                            IntegerExpression(3))), 150)