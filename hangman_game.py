import random

# Predefined list of 5 words
words = ["apple", "banana", "grape", "mango", "lemon"]

# Select a random word
selected_word = random.choice(words)
guessed_word = ["_"] * len(selected_word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word. You have 6 incorrect guesses.")

while attempts > 0 and "_" in guessed_word:
    print("\nCurrent word: ", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try a different one.")
        continue

    guessed_letters.append(guess)

    if guess in selected_word:
        print("Good guess!")
        for index, letter in enumerate(selected_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", selected_word)
else:
    print("\nOut of attempts! The word was:", selected_word)
