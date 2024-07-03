from bakery import assert_equal
from monster_mash import Media, party1, party2, party3, party4







assert_equal(last_song(party1.media), "no songs")
assert_equal(last_song(party2.media), "Werewolves of London")
assert_equal(last_song(party3.media), "Hedwig's Theme")
assert_equal(last_song(party4.media), "Oogie Boogie's Song")