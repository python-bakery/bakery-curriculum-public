from bakery import assert_equal
from monster_mash import Party, party1, party2, party3, party4







assert_equal(get_party_ratio(party1.party), 0.0)
assert_equal(get_party_ratio(party2.party), 3/5)
assert_equal(get_party_ratio(party3.party), 35/100)
assert_equal(get_party_ratio(party4.party), 230/300)