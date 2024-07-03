from bakery import assert_equal


def double_elements(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.append(number*2)
    return result

test1 = [1, 2, 3]
assert_equal(double_elements(test1), [2, 4, 6])
assert_equal(test1, [1, 2, 3])

test2 = [6, 4, 5]
assert_equal(double_elements(test2), [12, 8, 10])
assert_equal(test2, [6, 4, 5])