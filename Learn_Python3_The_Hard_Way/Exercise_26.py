# Learn Python The Hard Way: Exercise 26
# Luis Fernando Koh Avila
# Data 2 B

def break_words(stuff):
  """This function will break up words for us."""
  words = stuff.split(' ') ## Check
  return words

def sort_words(words):
  """Sorts the words."""
  return sorted(words)

# def print_first_word(words)
def print_first_word(words): # Important to add ":" at the end of a function
  """Prints the first word after popping it off."""
   # word = words.poop(0)
  word = words.pop(0) # Change poop for pop
  # print word
  print(word) # Necessary the use of parentheses

def print_last_word(words):
  """Prints the last word after popping it off."""
  # word = words.pop(-1
  word = words.pop(-1) # Add parentesis at the end
  # print word
  print(word) # Define the variable we want to print on screen

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# print "Let's practice everything."
print("Let's practice everything.")
#print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

# print "--------------"
print("--------------") # Necessary the use of parentheses
# print poem
print(poem) # Define the variable we want to print on screen and necessary use of parentheses
# print "--------------"
print("--------------") # Necessary the use of parentheses

# five = 10 - 2 + 3 - 5
five = 10 -2 + 2 - 5 # Giving the correct 5 value

# print "This should be five: %s" % five
print(f"This should be five: %s" % five) # Necessary the use of parentheses

def secret_formula(started):
  jelly_beans = started * 500
  # jars = jelly_beans \ 1000
  jars = jelly_beans / 1000 # Change \ for / to make a division
  crates = jars / 100
  return jelly_beans, jars, crates


start_point = 10000

# beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point)
# Use the "_" instead of "-", change beans for jelly_beans and use only one =

# print "With a starting point of: %d" % start_point
print("With a starting point of: %d" %start_point) # Necessary the use of parentheses

# print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)) # Necessary the use of parentheses

start_point = start_point / 10

# print "We can also do that this way:"
print("We can also do that this way:")  # Necessary the use of parentheses
# print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont

print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))
# Necessary the use of parentheses, change to start_point and add a parentheses at the end

# sentence = "All god\tthings come to those who weight."
sentence =("All good things come to those who weight.")
# Necessary the use of parentheses and correct wrong spelling

# words = ex25.break_words(sentence)
words = break_words(sentence) # Correcting the variable ex25 doesn't have any sense
# sorted_words = ex25.sort_words(words)
sorted_words = sort_words(words) # Correcting the variable ex25 doesn't have any sense
print_first_word(words)
print_last_word(words)
# .print_first_word(sorted_words)
print_first_word(sorted_words) # Print without a point at the beginning
print_last_word(sorted_words)
# sorted_words = ex25.sort_sentence(sentence)
sorted_words = sort_sentence(sentence) # Correcting the variable ex25 doesn't have any sense
# prin sorted_words
print(sorted_words) # Correct the print adding parentheses
# print_irst_and_last(sentence)
print_first_and_last(sentence) # Correct the spelling of the variable
# print_first_a_last_sorted(senence)
print_first_and_last_sorted(sentence) # Passing correct function name
