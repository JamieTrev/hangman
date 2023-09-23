import random

print("Welcome to Hangman")
print("----------------------------------------")

wordDictionary = [
    "project",
    "monkey",
    "python",
    "sunflower",
    "coffee",
    "mouse",
    "picture",
    "school",
    "sandwich",
    "definition"
]

randomWord = random.choice(wordDictionary)
randomWord = randomWord.lower()

for x in randomWord:
    print("_", end=" ")


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
        """
    ]
    print(hangman_images[wrong])


def printWord(guessedLetters):
    for char in randomWord:
        if char in guessedLetters:
            print(char, end=" ")
        else:
            print("_", end=" ")


def printLines():
    print("\n" + "\u203E " * len(randomWord))


length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_letters_guessed = []
current_letters_right = 0

while amount_of_times_wrong != 6:
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")

    letterGuessed = input("\nGuess a letter: ").lower()

    if letterGuessed in current_letters_guessed:
        print("You have already guessed that letter.")
        continue
    current_letters_guessed.append(letterGuessed)

    if letterGuessed in randomWord:
        current_letters_right = sum(1 for char in randomWord if char in current_letters_guessed)  # noqa
        printWord(current_letters_guessed)
        printLines()

        if current_letters_right == length_of_word_to_guess:
            print("\nCongratulations! You've guessed the word: " + randomWord)
            break  # Exit the loop as the game is won
    else:
        amount_of_times_wrong += 1
        print_hangman(amount_of_times_wrong)
        printWord(current_letters_guessed)
        printLines()

if amount_of_times_wrong == 6:
    print("\nSorry, you've run out of attempts. The word was:", randomWord)

print("Game is over! Thank you for playing :)")
