def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        print("match!")
    else:
        print("No Match!")


check_first_letter(word="happy", letter="i")
