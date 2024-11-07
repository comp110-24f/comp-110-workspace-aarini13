"""File to define Fish class."""


class Fish:
    """Only fish attribute we care abt is how old they are."""

    age: int

    def __init__(self):
        """Initializes a new fish in the river."""
        self.age = 0
        return None

    def one_day(self):
        """After one day, the fish ages by a day."""
        self.age += 1
        return None
