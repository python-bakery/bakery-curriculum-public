from bakery import assert_equal

# NOTE
# Assume that the split_pay function is already defined!
# Do NOT write split_pay yourself!
# ONLY write the assert_equal statements below!

assert_equal(split_pay("$5.00", 5), 1.0)
assert_equal(split_pay("$.00", 5), 0.0)
assert_equal(split_pay(".00", 5), 0.0)
assert_equal(split_pay("$.00", 0), 0.0)
assert_equal(split_pay("..900", 1), 0.0)
#assert_equal(split_pay("...900", 1), 0.0)
assert_equal(split_pay("$$9", 1), 0.0)
#assert_equal(split_pay(___), ___)
# ... Write some more too!