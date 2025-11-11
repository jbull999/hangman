def main():
    """Hangman game -
    The first player chooses a secret word and draws a blank line for each letter
    in the word e.g. if the secret word is "cats", there are 4 blank spots "_ _ _ _".
    Now the other player starts guessing the secret word by naming a single letter.
    If the letter occurs in the secret word, the first player fills in this letter
    at all spots e.g. secret word "cats", first guess is "a" then "_ a _ _".
    Whenever the letter does not occur in the secret word, the first player draws
    a part of the hangman figure.  The parts are traditionally drawn in this order:
      Post (upside-down "L")
      Head (circle)
      Back (straight line from the head downwards)
      One arm
      Second arm
      One leg
      Second leg
      Rope
    The game ends, when either the second player has guessed the secret word,
    or the hangman drawing is finished (8 wrong guesses)."""

    def get_word():
        print("Welcome to the Hangman Game!")
        print("This is a 2 player game, where one player defines a secret word and the other player guesses the secret word.")
        print("Player 1 - Think of a secret word.")
        word = input("Enter secret word...").upper()


    def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 8



    guesses = ""
    guesses += guess.upper()

    tries = 8
    while tries > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
            if failed == 0:
                print("You win!  You guessed the secret word!")
                break

    if guess not in word:
        print("Sorry, that letter is not in the secret word.")
        tries -= 1
        print("Player 2 - You have ", turn, "more guesses.")

        if guesses == 0:
            print("Player 2: You lose!  You did not guess the secret word!")


    while guesses not in word:
        print

# Hangman ASCII art stages (from 0 mistakes to 6 mistakes)
def Hangman():
    HANGMAN_PICS = [
        """ 
        """,
        """
         +---+
             |
             |
             |
             |
            ===
        """,
        """
         +---+
             |
         O   |
             |
             |
            ===
        """,
        """
         +---+
             |
         O   |
         |   |
             |
            ===
        """,
        """
         +---+
             |
         O   |
        /|   |
             |
            ===
        """,
        """
         +---+
             |
         O   |
        /|\  |
             |
            ===
        """,
        """
         +---+
             |  
         O   |
        /|\  |
        /    |
            ===
        """,
        """
         +---+
             |    
         O   |
        /|\  |
        / \  |
            ===
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
            ===
        """
    ]

# Example usage
mistakes = 3
print(HANGMAN_PICS[mistakes])



if __name__ == "__main__":
    main()


