import random

print("Welcome to Hangman")
print("----------------------------------------")

wordDictionary = ["project", "monkey", "book", "sunflower", "coffee", "mouse", "picture", "school",
"sandwich", "definition"]

### Choose a random word
randomWord = random.choice(wordDictionary)