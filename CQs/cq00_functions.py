"""Challenge Question 00"""

__author__ = "730550999"


def mimic(message: str) -> str:
    """Reply what is inputted."""
    return message


mimic("hello")


def main() -> None:
    """Pulls together functions into one main function"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
