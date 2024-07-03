from cisc108 import assert_equal
from string import ascii_letters

def starts_with_letter(text: str) -> bool:
    return text[0] in ascii_letters

assert_equal(starts_with_letter("TEST"), True)
assert_equal(starts_with_letter("!?!?"), False)
assert_equal(starts_with_letter("45 is evil"), False)
