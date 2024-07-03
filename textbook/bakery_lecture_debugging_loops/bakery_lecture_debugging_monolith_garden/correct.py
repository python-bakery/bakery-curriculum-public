from bakery import assert_equal

def biggest_bed(garden: str) -> str:
    # Wrong guard check
    if not garden:
        return "no flowers"
    flower_beds = garden.split(',')
    most_popular = flower_beds[0]
    taking = True
    for flower_bed in flower_beds:
        if '🌳' in flower_bed:
            taking = False
        elif taking and '🌱' not in flower_bed:
            # Logic should be `and`, not `or`
            if len(flower_bed) > len(most_popular) or '🌱' in most_popular:
                # Flipped assignment order
                most_popular = flower_bed
    # Bad use of `or`
    if '🌱' in most_popular or '🌳' in most_popular:
        return "no flowers"
    return most_popular

assert_equal(biggest_bed("🌹🌹,🌷🌷,🌻🌻🌻,🌸"), "🌻🌻🌻")
assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌺🌺🌺🌺")
assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌱🌱🌱🌱🌱,🌳,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌼🌼🌼")
assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌳,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌼🌼🌼")
assert_equal(biggest_bed("🌹🌹,🌷🌷,🌼🌼🌼,🌱🌱🌱🌱🌱,🌸,🌺🌺🌺🌺,🌻🌻🌻"), "🌺🌺🌺🌺")
assert_equal(biggest_bed("🌱🌱,🌱🌱🌱,🌳,🌸,🌺🌺🌺🌺"), "no flowers")
assert_equal(biggest_bed("🌳,🌸,🌺🌺🌺🌺"), "no flowers")
assert_equal(biggest_bed(""), "no flowers")
assert_equal(biggest_bed("🌳🌳🌳"), "no flowers")
assert_equal(biggest_bed("🌱🌱"), "no flowers")
assert_equal(biggest_bed("🌱🌱🌱,🌹🌹🌹🌹"), "🌹🌹🌹🌹")