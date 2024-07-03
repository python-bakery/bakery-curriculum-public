import matplotlib.pyplot as plt
from bakery_canvas import get_submissions
from datetime import datetime

def days_apart(first_date: str, second_date: str) -> int:
    """
    Determines the days between `first` and `second` date.
    Do not modify this function!
    """
    first_date = datetime.strptime(first_date, "%Y-%m-%dT%H:%M:%S%z")
    second_date = datetime.strptime(second_date, "%Y-%m-%dT%H:%M:%S%z")
    difference = second_date - first_date
    return difference.days

#  ...

plot_earliness('annie', 100167)
plot_earliness('abed', 100167)
plot_earliness('jeff', 100167)