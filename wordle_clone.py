# create a game that will pick a 5 letter word and the user will have to guess it
# the user will have 10 guesses to get the word
# if the user guesses the word correctly, the user wins
# input comes from the terminal
# output goes to the terminal

import random

def processInput(theAnswer, theGuess):
  position = 0
  clue = ""
  for letter in theGuess:
    if letter == theAnswer[position]:
      clue += "G"
    elif letter in theAnswer:
      clue += "Y"
    else:
      clue += "-"
    position += 1
  print(clue)
  return clue == "GGGGG" #True of correct, False otherwise

word_list = []
word_file = open("words.txt", "r")
for word in word_file:
    word_list.append(word.strip())
    
#pick a random word from the list
anwser = random.choice(word_list)

num_of_guesses = 0
guessed_correctly = False

while num_of_guesses < 10 and not guessed_correctly:
    guess = input("Guess a 5 letter word: ")
    print("You have guessed", guess)
    num_of_guesses += 1
    
    guessed_correctly = processInput(anwser, guess)
        

# if the user guessed correctly, print a message
if guessed_correctly:
    print("You guessed correctly!")
else : # otherwise, print a message
    print("You ran out of guesses. The word was " + anwser)