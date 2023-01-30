# Hangman_game

from random import choice

# Create a list of words
words = ['bat', 'cat', 'dog', 'rat', 'fox', 'cow']

# Select a random word from the list
word = choice(words)

# Initialize the lives counter
lives = 6

# Create a list to store the letters guessed
guessed_letters = []

# Create a string of underscores to show the progress of the game
progress = '_' * len(word)

# Print the initial progress
print(f'The word is {progress}')

while True:

    # Ask the user for a letter
    letter = input('Guess a letter: ').lower()

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        print('You have already guessed that letter')
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(letter)

    # Check if the letter is in the word
    if letter in word:
        print('Correct!')
        # Update the progress string
        new_progress = ''
        for i in range(len(word)):
            if letter == word[i]:
                new_progress += letter
            else:
                new_progress += progress[i]
        progress = new_progress
    else:
        print('Incorrect!')
        lives -= 1

    # Print the progress
    print(progress)
    print(f'You have {lives} lives remaining')

    # Check if the game is over
    if lives == 0:
        print('You lose!')
        break
    if '_' not in progress:
        print('You win!')
        break