"""a cute step to wordle <3"""

__author__ = "730550999"


def input_word() -> str:
    guess_word = str(input("Enter a 5-character word: "))
    if len(guess_word) != 5:  # could also do it reverse way where len == 5
        print("Error: Word must contain 5 characters.")
        exit()
        return guess_word
    else:
        print(guess_word)
        return guess_word


def input_letter() -> str:
    guess_letter = str(input("Enter a single character: "))
    if len(guess_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
        return guess_letter
    else:
        return guess_letter


def contains_char(word=input_word(), letter=input_letter()) -> None:
    print("Searching for " + letter + " in " + word)
    letter_index: int = 0
    count: int = 0  # need both in order to keep track of different variables
    while letter_index <= 4:  # too complex to put the length of the word inputter
        if letter == word[letter_index]:
            print(str(letter) + " found at index " + str(letter_index))
            letter_index += 1
            count += 1
        else:
            letter_index += 1
    if count >= 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print(
            "No instances of " + letter + " found in " + word
        )  # if else after while to ensure the count is completed


"""inputs in function not needed since it will ask question twice"""


def main() -> None:
    contains_char()


if __name__ == "__main__":
    main()
