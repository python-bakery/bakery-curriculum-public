from bakery import assert_equal

def remove_xs(values: [str]) -> [str]:
    result = []
    for value in values:
        if value != "x":
            result.append(value)
    return result

def map_strs_to_ints(values: [str]) -> [int]:
    result = []
    for value in values:
        result.append(int(value))
    return result

def summate(values: [int]) -> int:
    total = 0
    for value in values:
        total = total + value
    return total

