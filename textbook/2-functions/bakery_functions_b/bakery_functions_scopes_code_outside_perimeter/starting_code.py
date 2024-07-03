from bakery import assert_equal

def calculate_perimeter(width: int, height: int) -> int:
    perimeter = width *2 + height * 2
    
calculate_perimeter(4, 3)

assert_equal(perimeter, 14)