from cisc108 import assert_equal

def begins_with_vowel(text: str) -> bool:
    return text[0] in "AEIOUaeiou"

assert_equal(begins_with_vowel("Hello"), False)
assert_equal(begins_with_vowel("hello"), False)
assert_equal(begins_with_vowel("apple"), True)
assert_equal(begins_with_vowel("Apple"), True)
