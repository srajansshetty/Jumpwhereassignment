import random

def generate_secret_number():
  """Generates a random 4-digit number with no repeated digits."""
  secret_number = ""
  while len(secret_number) < 4:
    digit = random.randint(0, 9)
    if digit not in secret_number:
      secret_number += str(digit)
  return secret_number

def calculate_cows_and_bulls(secret_number, guess):
  """Calculates the number of cows and bulls in a guess."""
  cows = 0
  bulls = 0
  for i in range(4):
    if secret_number[i] == guess[i]:
      cows += 1
    elif secret_number[i] in guess:
      bulls += 1
  return cows, bulls

def play_cows_and_bulls():
  """Plays the Cows and Bulls game with the user."""

  secret_number = generate_secret_number()
  num_guesses = 0

  print("Welcome to the Cows and Bulls Game!")

  while True:
    guess = input("Enter a number: ")

    # Validate the guess.
    if len(guess) != 4 or any(digit in guess for digit in range(10) if guess.count(digit) > 1):
      print("Invalid guess. Please enter a 4-digit number with no repeated digits.")
      continue

    # Calculate the cows and bulls.
    cows, bulls = calculate_cows_and_bulls(secret_number, guess)

    # Tell the user the results of their guess.
    print(f"{cows} cows, {bulls} bulls")

    # If the user guessed the correct number, the game is over.
    if cows == 4:
      break

    # Increment the number of guesses.
    num_guesses += 1

  print(f"Congratulations! You guessed the correct number in {num_guesses} guesses.")

if __name__ == "__main__":
  play_cows_and_bulls()