import WordsDB


class Word:
    word_to_be_guessed = ""
    guess_list = []
    game_wins = 0
    game_losses = 0


graphics = (" _______\n |     |\n |\n |\n |\n |\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |\n |\n |\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |     |\n |\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |    /|\n |\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |    /|\\\n |\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |    /|\\\n |     ^\n |\n |\n |\n---",
            " _______\n |     |\n |     O\n |    /|\\\n |     ^\n |    /\n |\n |\n---",
            " _______\n |     |\n |     O\n |    /|\\\n |     ^\n |    / \\\n |\n |\n---")


def check_guess(guess):
    if len(guess) != 1:
        return False
    if guess in Word.guess_list:
        return False

    Word.guess_list.append(guess)
    return True


""" Takes players guess and applies the letter to
    the word player is searching for """

def correct_letter(repeated_times, guess, letters_guessed):
    # If there are multiple letters the same as the guessed letter
    # find all the indices in the word for that letter and replace
    # them with that letter
    if repeated_times > 1:
        temp_word = Word.word_to_be_guessed
        for x in range(repeated_times):
            index = temp_word.index(guess)
            letters_guessed = letters_guessed[:index] + guess + letters_guessed[index + 1:]
            temp_word = temp_word.replace(guess, ' ', 1)
    # Find the index for the guessed letter and place the letter in the word
    else:
        index = Word.word_to_be_guessed.index(guess)
        letters_guessed = letters_guessed[:index] + guess + letters_guessed[index + 1:]

    return letters_guessed


def get_guess(wrong_guesses, letters_guessed):
    print(graphics[wrong_guesses])
    print("Guessed Letters: " + str(Word.guess_list))
    print("Word: " + letters_guessed + "\n")
    guess = str(input("Guess A Letter: "))

    return guess


""" Loops till player has too many wrong guesses or until
    player guesses the word """

def guess_loop(wrong_guesses, letters_guessed):
    while wrong_guesses < 7:
        if letters_guessed == Word.word_to_be_guessed:
            return True

        # Get player guess and check correctness
        guess = get_guess(wrong_guesses, letters_guessed)
        if not check_guess(guess):
            wrong_guesses = wrong_guesses + 1
            continue

        # If player guess correct, places players guesses into string
        # (String used for display)
        # If player guess incorrect, move down the hangman phases
        if guess in Word.word_to_be_guessed:
            repeated_times = Word.word_to_be_guessed.count(guess)  # Get number of times letter is repeated in word
            letters_guessed = correct_letter(repeated_times, guess, letters_guessed)
        else:
            wrong_guesses = wrong_guesses + 1

        print("\n\n")
    return False


def make_guesses():
    letters_guessed = "_" * (len(Word.word_to_be_guessed))
    wrong_guesses = 0

    return guess_loop(wrong_guesses, letters_guessed)


def print_success():
    Word.game_wins = Word.game_wins + 1
    print("\n\n\n")
    print("###########################\n"
          "######### Success #########\n"
          "###########################")
    print("\n\n\n")


def print_loss():
    Word.game_losses = Word.game_losses + 1
    print("\n\n\n")
    print(graphics[7])
    print("Correct Word: " + Word.word_to_be_guessed)
    print("##########################\n"
          "########## Loss ##########\n"
          "##########################")
    print("\n\n\n")


def play_again():
    play = str(input("Would you like to play again [y/n]: "))
    if play == "y":
        Word.guess_list = []  # To reset "already guessed letters" list
        hangman_steps()


def hangman_steps():
    print("\n\nWelcome Player!!\nYou Have 7 Guesses\n\n")

    Word.word_to_be_guessed = WordsDB.get_ran_word()
    # print(Word.word_to_be_guessed)  # For testing only
    is_successful = make_guesses()

    if is_successful:
        print_success()
    else:
        print_loss()

    play_again()
    print("Game Wins: "+str(Word.game_wins))
    print("Game Losses: "+str(Word.game_losses))
    print("\nThanks For Playing!")


hangman_steps()
