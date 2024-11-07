"""File to define River class!"""

__author__ = "730550999"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """New class of river that pulls from fish and bear classes."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())
        """By appending, we are initializing a new bear in the class."""

    def check_ages(self):
        """Ages of bears and fish, we don't want them too old."""
        bearlist: list = []
        fishlist: list = []
        for fish in self.fish:
            if fish.age <= 3:
                fishlist.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                bearlist.append(bear)
        self.fish = fishlist
        self.bears = bearlist
        return None

    def remove_fish(self, amount: int) -> None:
        """Fish removed when eaten."""
        index: int = 0
        while index < amount:
            self.fish.pop(0)
            index += 1

    def bears_eating(self):
        """Bear eats 3 fish."""
        index: int = 0
        while index < len(self.bears):
            if len(self.fish) >= 5:
                self.remove_fish(3)
                self.bears[index].eat(3)
            index += 1
        return None

    def check_hunger(self):
        """If hunger of bear is negative they should die."""
        newbears: list = []
        index: int = 0
        while index < len(self.bears):
            if self.bears[index].hunger_score >= 0:
                newbears.append(self.bears[index])
            index += 1
        self.bears = newbears
        return None

    def repopulate_fish(self):
        """One pair of fish = 4 children."""
        n = len(self.fish)
        children: int = (n // 2) * 4
        index: int = 0
        while index < children:
            self.fish.append(Fish())
            index += 1
        return None

    def repopulate_bears(self):
        """One pair of bears = 1 child."""
        n = len(self.bears)
        child: int = n // 2
        index: int = 0
        while index < child:
            self.bears.append(Bear())
            index += 1
        return None

    def view_river(self):
        """Easier to use f-strings."""
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river!"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One week is just the one day function running 7 times."""
        round: int = 0
        while round < 7:
            self.one_river_day()
            round += 1
