from bakery import assert_equal

def find_halfway(text: str) -> int:
    return int(len(text)/2)


assert_equal(find_halfway("Banana"), 3)
assert_equal(find_halfway("ABCDEFG"), 3)
assert_equal(find_halfway("Half & Half"), 5)

assert_equal(chop_half("Banana"), "Ban")
assert_equal(chop_half("ABCDEFG"), "ABC")
assert_equal(chop_half("Half & Half"), "Half ")
