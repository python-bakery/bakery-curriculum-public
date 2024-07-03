from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Grocery:
    item: str
    cost: int
    on_sale: bool

