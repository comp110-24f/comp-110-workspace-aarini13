"""practice using while loops in code"""

__author__ = "730550999"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    letter: int = 0
    while letter < len(phrase):
        if search_char == phrase[letter]:
            count += 1
            letter += 1
        else:
            letter += 1  # don't need to reiterate count, it will just stay the same
    return count


print(
    num_instances(phrase="HelloHelloHEllo", search_char="e")
)  # print function is used because the function just returns the number but print gives it back to the person
