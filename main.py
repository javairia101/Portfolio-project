import random
import sys

def load_words(filename):
    try:
        with open(filename, "r") as file:
            words = []
            for line in file:
                word = line.strip()
                if word.isalpha():
                    words.append(word)
        return words
    except FileNotFoundError:
        print("word file not found")
        return []

def play_game(words):
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    hangman = [
        """
        +---+
        ¦   ¦
        0   ¦
      / ¦ \ ¦
       / \  ¦
       ========
        """,
        """
        +---+
        ¦   ¦
        0   ¦
       /¦\  ¦
       /¦   ¦
       ========
        """,
        """
        +---+
        ¦   ¦
        0   ¦
       /¦\  ¦
            ¦
       ========
        """,
        """
        +---+
        ¦   ¦
        0   ¦
       /¦   ¦
            ¦
       ======
        """,
        """
        +---+
        ¦   ¦
        0   ¦
        ¦   ¦
            ¦
        ======
        """,
        """
        +---+
        ¦   ¦
        0   ¦
            ¦
            ¦
        =====
        """,
        """
        +---+
        ¦   ¦
            ¦
            ¦
            ¦
        =====
        """
    ]
    print("Welcome to hangman!")
    while wrong_guesses < 6:
        print(hangman[wrong_guesses])
        print("word:", display_word)
        print("Attempts left:", 6 - wrong_guesses)


        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + ""
            else:
                display += "_ "

        print("word:", display)
        print("Attempts left:", 6 - wrong_guesses)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter!")
            continue
        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("You won!")
            return True, word
    print(hangman[6])
    print("Game over!")
    print("The word was:", word)
    return False, word

def save_result(won, word):
    try:
        with open("results.txt", "a") as file:
            if won:
                file.write("won: " + word + "\n")
            else:
                file.write("lost: " + word + "\n")
        print("result saved")
    except OSError:
        print("result not saved")

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "words.txt"
    words = load_words(filename)
    if not words:
        return

    won , word = play_game(words)
    save_result(won, word)
main()

