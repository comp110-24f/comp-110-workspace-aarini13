"""Practice writing functions based on in class concepts"""

__author__ = "730550999"


def main_planner(guests: int) -> None:
    """summary of values"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """each person gets two tea bags"""
    return people * 2


def treats(people: int) -> int:
    """each tea gets 1.5 treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """total cost for tea bags and treats"""
    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
