from words import level_words


def define_level() -> list:
    levels_count: int = len(level_words)
    level_input: str = input(f"Choise level, max {levels_count}\n")

    is_numeric: bool = level_input.isnumeric()
    if not is_numeric:
        print("The value is not a word!!")
        return define_level()

    level_input_number: int = int(level_input) - 1
    if level_input_number > levels_count or level_input_number < 0:
        print("The value is not allowed!!")
        return define_level()

    return level_words[level_input_number]
