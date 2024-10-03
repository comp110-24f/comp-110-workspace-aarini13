"""wordleee"""

__author__ = "730550999"


def main(secret: str) -> None:
    """the entrypoint of the program and main game loop"""
    num_turns: int = 1
    win: bool = False
    while num_turns <= 6 and win == False:
        print(f"=== Turn {num_turns}/6 ===")
        boxes: str = emojified(
            guess=input_guess(secret_word_len=len(secret)), secret_word=secret
        )  # easier to just make a local variable for this
        if boxes == str(len(secret) * "\U0001F7E9"):
            print(f"You won in {num_turns}/6 turns!")
            win = True
        else:
            num_turns += 1
    if num_turns > 6:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # if-else statement in case the if exits into this


def input_guess(secret_word_len: int) -> str:
    guess_word: str = str(input(f"Enter a {secret_word_len} character word: "))
    while len(guess_word) != secret_word_len:
        guess_word = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
    return guess_word


def contains_char(check_word: str, check_letter: str) -> bool:
    """the purpose of this function is to check if a certain letter is in a word"""
    assert len(check_letter) == 1
    letter_index: int = 0
    letter_count: int = 0
    while letter_index < len(check_word):
        if check_letter == check_word[letter_index]:
            letter_count += 1
            letter_index += 1
        else:
            letter_index += 1
    if letter_count >= 1:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """function: check if the guessed word matches the secret word at each index"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index_letter2: int = 0
    emojis = str()
    while index_letter2 < len(secret_word):
        if guess[index_letter2] == secret_word[index_letter2]:
            emojis += GREEN_BOX
            index_letter2 += 1
        elif (
            contains_char(check_word=secret_word, check_letter=guess[index_letter2])
            is True
        ):
            emojis += YELLOW_BOX
            index_letter2 += 1
        else:
            emojis += WHITE_BOX
            index_letter2 += 1
    print(emojis)  # print here instead of main function makes it easier code wise
    return emojis


if __name__ == "__main__":
    main(secret="codes")
