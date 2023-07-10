#Bagels, by Al Sweigart
#Deductive logic game where you must guess a number based on clues

import random
NUM_Digits = 3
Max_Guesses = 10

def main():
  print ('''Bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:       That means:
  Pico             One digit is correct but in the wrong position
  Fermi            One digit is correct and in the right position.
  Bagels           No digit is correct
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_Digits))
  while True: #Main Game Loop
    # This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print(' You have {} guesses to get it.'.format(Max_Guesses))
    numGuesses = 1
    while numGuesses <= Max_Guesses:
      guess = ''
      # Keep looping until they enter a valid guess:
      while len(guess) != NUM_Digits or not guess.isdecimal():
        print('Guess #{} '.format(numGuesses))
        guess = input('> ')
      clues = getClues(guess, secretNum)
      print(clues)
      numGuesses +=1
      if guess == secretNum:
        break #They're Correct, so break out of this loop.
      if numGuesses > Max_Guesses:
        print("You ran out of guesses")
        print('The answer was {}.'.format(secretNum))
    #Ask Player if they want to play again
    print('Do you want to play again? (yes or no)')
    if not input('>').lower().startswith('y'):
      break
  print('Thanks for Playing')


def getSecretNum():
  """ Returns a string made up of NUM_DIGITS unique random digits."""
  numbers   = list('0123456789')
  random.shuffle(numbers) # Shuffle them into random order
  #Get the first num_digits digits in the list for the secret number:
  secretNum = ''
  for i in range(NUM_Digits):
    secretNum += str(numbers[i])
  return secretNum

def getClues(guess, secretNum):
  """ Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
  if guess == secretNum:
    return "You got it !"
  clues = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      #A correct digit is in the correct place.
      clues.append('Fermi')
    elif guess [i] in secretNum:
      #A correct digit is in the incorrect place.
      clues.append('Pico')
  if len(clues) ==0:
    return 'Bagels'
  else:
    #Sort the clues into alphabetical order so their original order
    #doesnt give information away
    clues.sort()
    # Make a single string from the list of string clues.
    return ''.join(clues)
if __name__ == '__main__':
  main()
