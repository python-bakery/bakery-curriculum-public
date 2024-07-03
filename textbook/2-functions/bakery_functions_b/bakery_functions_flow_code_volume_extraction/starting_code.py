from bakery import assert_equal

PI = 3.14159

def calculate_area(radius: float) -> float:
    pass

def calculate_volume(radius: float, height: float) -> float:
    pass


assert_equal(calculate_area(1.), PI)
assert_equal(calculate_area(5.), 78.53975)
assert_equal(calculate_area(2.), 12.56636)
assert_equal(calculate_volume(1., 2.), 2*PI)
assert_equal(calculate_volume(5., 1.), 78.53975)
assert_equal(calculate_volume(2., 3.1), 38.955716)
