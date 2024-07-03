from bakery import assert_equal

def swap_ends(numbers: list[int]) -> list[int]:
    if not numbers:
        return []
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers
    # Note example way that is incorrect because of the mutation checks
    #result = []
    #result.append(numbers[-1])
    #result.extend(numbers[1:-1])
    #if len(numbers) > 1:
    #    result.append(numbers[0])
    #return result

assert_equal(swap_ends([1,2,3]), [3,2,1])
assert_equal(swap_ends([3]), [3])
assert_equal(swap_ends([]), [])