#Number Guessing game
import random

# Generate a random number
number = random.randint(1, 10)

# Initialize the number of guesses
guesses = 0

# Ask the user for their guess
while True:
    guess = int(input('Guess a number between 1 and 10: '))

    # Increment the number of guesses
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print(f'You guessed correctly in {guesses} guesses!')
        break
    elif guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')