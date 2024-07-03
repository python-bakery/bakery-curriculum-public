from dataclasses import dataclass
from bakery import assert_equal






assert_equal(adopt(Person("Dr.", "Bart"), "Ada", "Dog"), Pet("Ada", "Bart", "Dog"))