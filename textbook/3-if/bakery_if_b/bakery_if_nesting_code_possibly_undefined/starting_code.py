from bakery import assert_equal

def calculate_income(salary: int) -> float:
    if salary > 5000:
        tax = .9
    return salary * tax

assert_equal(calculate_income(1000), 1000.0)
assert_equal(calculate_income(10000), 9000.0)