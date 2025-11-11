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

from numpy.ma.core import indices




def get_word():
    print("\nWelcome to the Hangman Game!")
    print("\nLets Play!")
    print("\nThis is a 2 player game, where one player defines a secret word and the other player guesses the secret word.")
    print("\nPlayer 1 - Think of a secret word.")
    word = input("Enter secret word...").upper()
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print(word_completion)
    print("Player 2 - You have ", tries, "more guesses.")
    while not guessed and tries > 0:
        guess = input("\nGuess a letter in the secret word").upper()
        if guess in guessed_letters:
            print("\nYou already guessed that letter.")
        elif guess not in word:
            print (guess, "\n is not in the secret word.")
            guessed_letters.append(guess)
            tries -= 1
            print("Player 2 - You have ", tries, "more guesses.")
            print(Hangman(tries))
        else:
            print("\nGood job!  You have guess a letter in the secret word.")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            print(word_completion)
            if "_" not in word_completion:
                guessed = True
                print("\nCongratualations!  You guessed it! \nThe secret word was", word_completion)


    while tries == 0:
        print("Player 2: You lose!  You did not guess the secret word! \nThe secret word is", word)
        break


# Hangman ASCII art stages (from 0 mistakes to 8 mistakes)
def Hangman(tries):
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

    return HANGMAN_PICS[::-1][tries]

return play(get_word())

def main():

    def play_again():
        while input("play again? (y/n): ").upper() == "Y":
            play(get_word())

if __name__ == "__main__":
    main()


