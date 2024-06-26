def get_draw(failed_attemps: int) -> str:
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========"""
    ]
    stages.reverse()
    return stages[failed_attemps]
