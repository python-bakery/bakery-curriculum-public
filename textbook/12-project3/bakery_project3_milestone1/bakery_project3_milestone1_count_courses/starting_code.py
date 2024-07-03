from bakery import assert_equal
from bakery_canvas import get_courses

def count_courses(user_token: str) -> int:
    pass

assert_equal(count_courses('annie'), 6)
assert_equal(count_courses('jeff'), 6)
assert_equal(count_courses('pierce'), 0)
assert_equal(count_courses('troy'), 1)