from bakery import assert_equal
from monster_mash import Potion, Ingredient, party1, party2, party3, party4







assert_equal(brew_time_per_ingredient(party1.brews), 0.0)
assert_equal(brew_time_per_ingredient(party2.brews), 17/8)
assert_equal(brew_time_per_ingredient(party3.brews), (56+29+5)/9)
assert_equal(brew_time_per_ingredient(party4.brews), 2.0)