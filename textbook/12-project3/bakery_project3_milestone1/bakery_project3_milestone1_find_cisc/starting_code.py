from bakery import assert_equal
from bakery_canvas import get_courses





assert_equal(find_cs1('annie'), 100167)
assert_equal(find_cs1('jeff'), 100167)
assert_equal(find_cs1('pierce'), 0)
assert_equal(find_cs1('troy'), 0)