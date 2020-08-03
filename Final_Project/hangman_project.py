import random

# Function that displays the Hangman according with the lives
def show_hangman(lives):
  if lives == 6:
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """)
  elif lives == 5:
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """)
  elif lives == 4:
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |   
                   -
                """)
  elif lives == 3:
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """)
  elif lives == 2:
    print("""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """)
  elif lives == 1:
    print("""
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """)
  elif lives == 0:
    print("""
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """)

# Function that prints the hide word and convert it to a list into a string
def print_hide(word):
  for i in range(0, len(word)):
    print(word[i],end="")
  print("\n")

# Take a random number from 1 to 1000
random_number = random.randrange(1000, 0, -1)

# Opening the .txt
f = open('words.txt', 'r')

# Ennumerates each word in the txt and takes the one that the random number
# chose
counter = 0
for word in f:
    counter += 1
    if random_number == counter:
      random_word = word[0:-1] # Save the word with slicing
      break

f.close() # Closing the file

word_length = len(random_word) # Takes the length from the random word
# print(f"Length: {word_length}")

hide_word = [] # Variable to store the hide word

# Loop that creates the word with the "*"
for i in range(0,word_length):
  hide_word.append('*') # Appending in a list the *

# Displaying the instructions
print("""
Luis Fernando Koh Avila
Data 2 B

                            Instructions
This is the classic Hangman Game, you have to write a letter in order
to find the word, you have 6 lives, if you lose all the lives game over.
Good luck, you'll need it.
The words are A to Z.
""")
# Variables
lives = 6 # Total lives
correct = 0 # Successes

show_hangman(lives) # Displaying the hangman
print("The word is: ", end = "") # Printing the word
print_hide(hide_word) # Calling function to print the currently word
print(f"Current lives: {lives}") # Showing the user the current lives

# Function to check if the typed character is correct
def check_character(character):
  if (character.isalpha() and len(character) == 1): # Check is in one character and a letter
    return True # Is is correct return True
  else:
    return False # If not return False

# Function to check if the player loose to display the message
def check_if_loose(lives):
  if lives == 0:
    print("GAME OVER")
    print(f"The word was: {random_word}")

while lives > 0 and word_length > 0: # Repeat the loop while accomplish the condition
  character = input("Type a letter: ").lower() # Ask for a letter, save it and convert it into lowercase
  
  checker = check_character(character) # Check the typed character by calling the function
  if checker == False:
    lives -= 1 # If is false the user loses a live
    show_hangman(lives) # Show the hangman
    print(f"Incorrect character, you have {lives} lives.") # Print current lives
    print_hide(hide_word) # Print the current hide word
    check_if_loose(lives) # Check if loose

  elif checker == True:
    # If is true then fill the hide word with the character
    if character in random_word and character not in hide_word: # Check if the word has already typed
      for i in range(0,len(word)): # Pass through each character in the list
        if(character == word[i]): # If the character is equal to letter in the original word 
          hide_word[i] = character # Then save it in the same location
          correct += 1 # Add 1 to the correct variable
      print_hide(hide_word) # And print the actualized hide word

    elif character in random_word and character  in hide_word:
      lives -= 1 # If the character has already typed then the user loses a live
      show_hangman(lives) # Show the hangman
      print(f"Same letter, you have {lives} lives.") # Print current lives
      print_hide(hide_word) # Print the current hide word
      check_if_loose(lives) # Check if loose

    else:
      lives -= 1 # If the letter are not in the word the user loses a live
      show_hangman(lives) # Show the hangman
      print(f"The letter are not in the word, you have {lives} lives.") # Print current lives
      print_hide(hide_word) # Print the current hide word
      check_if_loose(lives) # Check if loose
  
  if(correct == word_length): # Finally if the size of the word is equal to the correct variable
    print("Congratulations!! you won!!") # Then the user won and show a message
    break # And break the loop
