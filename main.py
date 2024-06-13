from level import define_level
from random import choice
from helpers import get_template, get_indexes


def hangman(sections: list, sections_count):
    if len(sections) == 0:
        return

    section: dict[str, str] = choice(sections)
    word: str = section["word"]
    hint: str = section["hint"]

    template_list: list = get_template(word)
    word_list: list = list(word)

    attempts: int = 6
    delimiter = ""

    while attempts > 0:
        print(f"Agreements: {delimiter.join(template_list)}. Attemps: {attempts}. Hint: {hint}")

        letters = input("Write a letter\n").lower()

        for letter in letters:
            if letter in template_list:
                attempts -= 1
                continue

            indexes = get_indexes(word_list, letter)
            for index in indexes:
                template_list[index] = letter

            if len(indexes) == 0:
                attempts -= 1
                continue

        if template_list == word_list:
            print(f"\nCongratulations! the word is '{word}'\n")
            sections.remove(section)
            return hangman(sections, sections_count)
    else:
        print(f"Game over!!")
        return


def run_game():
    sections = define_level()
    hangman(sections, len(sections))
    print(f"You win!!")
    again = input("\nDo you want to play again?, press Y to continue or any other key to quit\n").upper()
    if again == "Y":
        run_game()


if __name__ == '__main__':
    run_game()
