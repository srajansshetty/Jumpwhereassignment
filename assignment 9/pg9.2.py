def read_words_from_file(filename):
  """Reads a list of words from a file."""
  with open(filename, "r") as f:
    words = [line.strip() for line in f]
  return words


words = read_words_from_file("words.txt")

def random_word(words):
  """Returns a random word from the given list."""
  return words[random.randint(0, len(words) - 1)]

def guess_word(word):
  """Asks the user to guess the given word letter by letter."""
  hidden_word = ["_" for letter in word]

  # Keep track of the letters the user has guessed.
  guessed_letters = set()

  # Give the user 6 guesses.
  num_guesses = 6

  while num_guesses > 0:
    # Get the user's guess.
    guess = input("Guess a letter: ")

    # If the guess is already in the guessed_letters set, skip it.
    if guess in guessed_letters:
      continue

    # Add the guess to the guessed_letters set.
    guessed_letters.add(guess)

    # If the guess is correct, reveal the letter in the hidden word.
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          hidden_word[i] = guess

    # If the user guessed the whole word correctly, return the word.
    if all(letter in hidden_word for letter in word):
      return word

    # Otherwise, tell the user how many guesses they have left.
    num_guesses -= 1
    print(f"You have {num_guesses} guesses left.")

  # If the user ran out of guesses, return None.
  return None