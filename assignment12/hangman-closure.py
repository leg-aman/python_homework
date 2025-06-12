# hangman_closure.py

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        letter = letter.lower()
        if letter not in guesses:
            guesses.append(letter)

        word_display = ""
        for char in secret_word:
            if char.lower() in guesses:
                word_display += char
            else:
                word_display += "_"

        print("Current word:", word_display)

        if "_" not in word_display:
            return True
        else:
            return False

    return hangman_closure


def play_hangman():
    print("Welcome to the Hangman Game")

    secret_word = input("Type a secret word: ")

    hangman = make_hangman(secret_word)
    total_guesses = 0

    while True:
        letter = input("Guess a letter: ")
        if len(letter) != 1 or letter.isalpha() == False:
            print("Please enter just one letter.")
            continue

        total_guesses = total_guesses + 1

        result = hangman(letter)

        if result:
            print("🎉 You guessed it!")
            print("The word was:", secret_word.upper())
            print("Guesses used:", total_guesses)
            break
        else:
            print("🕹️ Try again\n")


play_hangman()