import random

MAX_ATTEMPTS = 6

WELCOME_MESSAGE = """
Welcome to Hangman
----------------------------------------
1 - You have 7 attempts to try to find the right word by
    inputting letters or the full word
2 - If you guess a wrong letter you will lose an attempt and the
    hangman will begin building
3 - When you reach 0 lives you will be hung and the game is over

GOOD LUCK!
----------------------------------------
"""


WORD_DICTIONARY = [
    "project",
    "monkey",
    "python",
    "sunflower",
    "coffee",
    "mouse",
    "picture",
    "school",
    "sandwich",
    "definition",
]


def print_hangman(wrong):
    """Prints the hangman based on the number of incorrect guesses.

    Args:
        wrong (int): The number of incorrect guesses made by the player.
    """
    hangman_images = [
        """
        +---+
            |
            |
            |
           ===
        """,
        """
        +---+
        O   |
            |
            |
           ===
        """,
        """
        +---+
        O   |
        |   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
       /    |
           ===
        """,
        """
        +---+
        O   |
       /|\  |
       / \  |
           ===
        """,
    ]
    print(hangman_images[wrong])


def print_current_word(current_word, guessedLetters):
    """Prints the current word with correctly guessed letters
    and underscores for unguessed letters.

    Args:
        current_word (str): The word to be guessed.
        guessedLetters (list[str]): List of letters guessed by the player.
    """
    for char in current_word:
        if char in guessedLetters:
            print(char, end=" ")
        else:
            print("_", end=" ")


def print_empty_lines(current_word):
    """Prints empty lines to separate word display.

    Args:
        current_word (str): The word to be guessed.
    """
    print("\n" + "\u203E " * len(current_word))


def print_current_guessed(current_letters_guessed):
    """Prints the letters guessed so far by the player.

    Args:
        current_letters_guessed (list[str]):
        List of letters guessed by the player.
    """
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")


def input_next_guess(current_letters_guessed):
    """Accepts user input and makes sure it is valid.

    Keeps asking for user input unless user enters a valid input.

    Args:
        current_letters_guessed (list[string]):
        List of currently guessed user inputs.

    Returns:
        string: A valid user input.
    """
    while True:
        user_input = input("\nGuess a letter: ").lower()

        if not user_input.isalpha():
            print("Only alphabets are allowed...")
            continue

        if len(user_input) > 1:
            print("Only enter one character..")
            continue

        if user_input in current_letters_guessed:
            print("You have already guessed that letter.")
            continue

        return user_input


def check_guessed_word(
    current_letters_guessed, current_word, user_input, current_letters_right
):
    """Checks if the guessed word is correct and updates the game state.

    Args:
        current_letters_guessed (list[str]):
        List of letters guessed by the player.
        current_word (str): The word to be guessed.
        user_input (str): The user's input guess.
        current_letters_right (int):
        The number of letters guessed correctly so far.

    Returns:
        True if the guessed word is correct, False otherwise.
    """
    current_letters_guessed.append(user_input)

    print_current_word(current_word, current_letters_guessed)
    print_empty_lines(current_word)
    if user_input in current_word:
        current_letters_right = sum(
            1 for char in current_word if char in current_letters_guessed
        )  # noqa

        if current_letters_right == len(current_word):
            print("\nCongratulations! You've guessed the word:" + current_word)
        return True
    else:
        return False


def main():
    """The main function to run the Hangman game."""
    amount_of_times_wrong = 0
    current_letters_guessed = []
    current_letters_right = 0

    print(WELCOME_MESSAGE)

    current_word = random.choice(WORD_DICTIONARY)
    current_word = current_word.lower()
    print_empty_lines(current_word)

    while amount_of_times_wrong != MAX_ATTEMPTS:
        print_current_guessed(current_letters_guessed)
        user_input = input_next_guess(current_letters_guessed)

        is_input_valid = check_guessed_word(
            current_letters_guessed,
            current_word,
            user_input,
            current_letters_right,
        )

        if not is_input_valid:
            amount_of_times_wrong += 1
            print_hangman(amount_of_times_wrong)

    if amount_of_times_wrong == MAX_ATTEMPTS:
        print(
            "\nSorry, you've run out of attempts. The word was:", current_word
        )

    print("Game is over! Thank you for playing :)")


if __name__ == "__main__":
    main()
