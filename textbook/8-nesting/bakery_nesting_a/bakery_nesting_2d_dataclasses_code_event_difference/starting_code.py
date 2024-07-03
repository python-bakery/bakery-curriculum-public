from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Time:
    hour: int
    minute: int
    
@dataclass
class Event:
    name: str
    start: Time
    stop: Time
