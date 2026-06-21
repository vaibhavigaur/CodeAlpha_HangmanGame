import random

list = ["python", "java", "django", "numpy"]

secret_word = random.choice(list)
guess_words = []
wrong_attempt = 0
max_attempt = 6

print("Welcome to HANGMAN GAME!")
print("Guess the word letter by letter.\n")
while wrong_attempt < max_attempt:
    display_words = ""

    for letter in secret_word:
        if letter in guess_words:
            display_words = display_words + letter + ""
        else:
            display_words += "_"

    print(f"Word: {display_words.strip()}")
    print(f"Wrong attempts are left: {max_attempt - wrong_attempt}")

    guess = input("Enter a word: ").lower()

    if guess in guess_words:
        print("You already guessed that words.\n")
        continue


    guess_words.append(guess)

    if guess not in secret_word:
        wrong_attempt += 1
        print("WRONG GUESS!\n")
    else:
        print("RIGHT GUESS!\n")

    all_guessed = True
    for letter in secret_word:
        if letter not in guess_words:
            all_guessed = False
            break

    if all_guessed:
        print(f"CONGRATULATIONS! You guessed the words: {secret_word}")
        break
if wrong_attempt == max_attempt:
    print(f"GAME OVER! The word was: {secret_word}")