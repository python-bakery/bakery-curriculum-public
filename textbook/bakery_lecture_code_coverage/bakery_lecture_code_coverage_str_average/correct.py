from bakery import assert_equal

assert_equal(add_three_digits("123"), 6)
assert_equal(add_three_digits("1!3"), 0)
assert_equal(add_three_digits(".."), 0)