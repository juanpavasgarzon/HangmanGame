def get_template(word: str) -> list:
    repeat: int = len(word)
    template: str = "_" * repeat

    return list(template)


def get_indexes(word_list: list, letter: str) -> set[int]:
    indexes: set[int] = set()
    for index, char in enumerate(word_list):
        if char == letter:
            indexes.add(index)

    return indexes
