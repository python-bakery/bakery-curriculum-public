from bakery import assert_equal
from monster_mash import Potion, Ingredient, party1, party2, party3, party4







assert_equal(get_rarest_potion(party1.brews), "N/A")
assert_equal(get_rarest_potion(party2.brews), "Lycansoup")
assert_equal(get_rarest_potion(party3.brews), "Pumpkin Spice Latte")
assert_equal(get_rarest_potion(party4.brews), "N/A")