
from bakery import assert_equal

# NOTE
# Assume that the numeric_day function is already defined!
# Do NOT write numeric_day yourself!
# ONLY write the assert_equal statements below!

assert_equal(numeric_day('tuesday'), 1)
assert_equal(numeric_day('Tuesday'), 1)
assert_equal(numeric_day('TUESDAY'), 1)
assert_equal(numeric_day('tues'), -1)
assert_equal(numeric_day('day'), -1)
assert_equal(numeric_day('saturday'), 5)