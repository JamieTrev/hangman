import random

MAX_ATTEMPTS = 6

WELCOME_MESSAGE = """
Welcome to
  _  _                                
 | || |__ _ _ _  __ _ _ __  __ _ _ _ 
 | __ / _` | ' \/ _` | '  \/ _` | ' \ 
 |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
                |___/
----------------------------------------
Can you work out what the hidden word is?

Guess 1 letter at a time but choose wisely
as any more than 6 incorrect guesses and
you'll be hung and the game is over!

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


def print_current_word(current_word, guessed_letters):
    for char in current_word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")


def print_empty_lines(current_word):
    print("\n" + "\u203E " * len(current_word))


def print_current_guessed(current_letters_guessed):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")


def input_next_guess(current_letters_guessed):
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


def check_guessed_word(current_letters_guessed, current_word, user_input):
    current_letters_guessed.append(user_input)

    if user_input in current_word:
        current_letters_right = sum(1 for char in current_word if char in current_letters_guessed)

        if current_letters_right == len(current_word):
            print("\nCongratulations! You've guessed the word:", current_word)
            return True
        return False
    else:
        return False


def main():
    play_again = True
    while play_again:
        amount_of_times_wrong = 0
        current_letters_guessed = []

        print(WELCOME_MESSAGE)

        current_word = random.choice(WORD_DICTIONARY)
        current_word = current_word.lower()

        while amount_of_times_wrong != MAX_ATTEMPTS:
            print_current_word(current_word, current_letters_guessed)
            print_empty_lines(current_word)
            print_current_guessed(current_letters_guessed)

            user_input = input_next_guess(current_letters_guessed)
            is_input_valid = check_guessed_word(current_letters_guessed, current_word, user_input)

            if is_input_valid:
                break
            else:
                if user_input not in current_word:
                    amount_of_times_wrong += 1
                    if amount_of_times_wrong != MAX_ATTEMPTS:
                        print_hangman(amount_of_times_wrong)
                    if amount_of_times_wrong == MAX_ATTEMPTS:
                        print("\nSorry, you've run out of attempts. The word was:", current_word)
                        break

        play_again_input = ""
        while play_again_input not in ["y", "n"]:
            play_again_input = input("\nDo you want to play again? (Y/N): ").lower()
            if play_again_input == "n":
                print("\nThanks for playing!\n")
                play_again = False
                break


if __name__ == "__main__":
    main()
