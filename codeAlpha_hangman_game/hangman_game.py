import random

# Simplified Hangman game
# - Uses a small list of 5 predefined words
# - Counts only incorrect guesses (limit 6)
# - Basic console input/output

MAX_INCORRECT = 6
WORDS = ["APPLE", "MANGO", "PEACH", "BERRY", "GRAPE"]

def play():
    secret = random.choice(WORDS)
    guessed_letters = []  # list of letters the player has guessed
    incorrect = 0

    print("WELCOME TO THE HANGMAN GAME")

    # loop until player has used up incorrect guesses or guessed the word
    while incorrect < MAX_INCORRECT and not all(ch in guessed_letters for ch in secret):
        # show progress with underscores for unguessed letters
        progress = "".join(ch if ch in guessed_letters else "_" for ch in secret)
        print("Word:", " ".join(progress))
        print(f"Incorrect guesses left: {MAX_INCORRECT - incorrect}")

        guess = input("Guess a letter (A-Z): ").strip().upper()

        # validate input: single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret:
            print("Good guess!\n")
        else:
            incorrect += 1
            print("Wrong guess.\n")

    # end game: check win/lose
    if all(ch in guessed_letters for ch in secret):
        print(f"Congratulations! You guessed the word: {secret}")
    else:
        print(f"Game over. The word was: {secret}")


play()
