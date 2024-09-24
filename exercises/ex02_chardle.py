"""a cute step to wordle <3"""

__author__ = "730550999"

"""inputs in function not needed since it will ask question twice"""


def main() -> None:
    word2: str = input_word()
    letter2: str = input_letter()
    contains_char(word=word2, letter=letter2)


def input_word() -> str:
    guess_word: str = str(input("Enter a 5-character word: "))
    if len(guess_word) != 5:  # could also do it reverse way where len == 5
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return guess_word


def input_letter() -> str:
    guess_letter = str(input("Enter a single character: "))
    if len(guess_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return guess_letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    letter_index: int = 0
    letter_count: int = 0  # need both in order to keep track of different variables
    while letter_index <= 4:  # too complex to put the length of the word inputter
        if letter == word[letter_index]:
            letter_count += 1
            print(str(letter) + " found at index " + str(letter_index))
            letter_index += 1
        else:
            letter_index += 1
    if letter_count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif letter_count > 1:
        print(str(letter_count) + " instances of " + letter + " found in " + word)
    else:
        print(
            "No instances of " + letter + " found in " + word
        )  # if else after while to ensure the count is completed


if __name__ == "__main__":
    main()
