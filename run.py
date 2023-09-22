import random

print("Welcome to Hangman")
print("----------------------------------------")

wordDictionary = [
    "project", 
    "monkey", 
    "book", 
    "sunflower", 
    "coffee",
    "mouse", 
    "picture", 
    "school", 
    "sandwich", 
    "definition"
]

### Choose a random word
randomWord = random.choice(wordDictionary)
randomWord = randomWord.lower()  # Convert the word to lowercase for case-insensitive matching

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
       /|\\  |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       /    |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       / \\  |
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

while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    ### Prompt user for input
    letterGuessed = input("\nGuess a letter: ").lower()  # Convert the guess to lowercase for case-insensitive matching
    ### Check if the letter has already been guessed
    if letterGuessed in current_letters_guessed:
        print("You have already guessed that letter.")
        continue
    current_letters_guessed.append(letterGuessed)
    ### User is right
    if letterGuessed in randomWord:
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    ### User is wrong
    else:
        amount_of_times_wrong += 1
        ### Update the drawing
        print_hangman(amount_of_times_wrong)
        printWord(current_letters_guessed)
        printLines()

print("Game is over! Thank you for playing :)")
