from bakery import assert_equal

def am_i_on_fire(temperature: int) -> bool:
    if (temperature > 109) == True:
        return True
    else:
        return False
    
assert_equal(am_i_on_fire(100), False)
assert_equal(am_i_on_fire(110), True)