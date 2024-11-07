"""File to define Bear class."""


class Bear:
    """Only attributes we care about in the bears."""

    age: int
    hunger_score: int

    def __init__(
        self,
    ):
        """Initializes a new bear in the river."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """After one day, the bears are a day older and they are hungrier."""
        self.age += 1
        self.hunger_score = self.hunger_score - 1
        return None

    def eat(self, num_fish: int) -> None:
        """After the bears eat a certain number of fish, it adds to hunger score."""
        self.hunger_score += num_fish
