# Luis Fernando Koh Avila
# Data 2 B

# CODE AFTER OPTIMIZATION

# Function to check if pass or fail
def calification(grade):
  if grade >= 7 and grade <= 10:
    print(f"Score: {grade} so you pass")
  elif grade < 7 and grade > 0:
    print(f"Score: {grade} so you fail")

# Luis scores for the first quarter
algorithms = [[9],[6],[7],[10]]
oral_expresion = [[10],[10],[5],[8]]
mathematics = [[9],[7],[7],[4]]
physics = [[6],[6],[5],[10]]

# For to call the function and know if pass of fail
print("\t\tFirst Quarter\n")
print("Algorithms Units Scores")
for grades in algorithms: # Check in the loop each score calling the function
  calification(grades[0])
print("-----------------------------------")
print("Oral Expresion Units Scores")
for grades in oral_expresion: # Check in the loop each score calling the function
  calification(grades[0])
print("-----------------------------------")
print("Mathematics Units Scores")
for grades in mathematics: # Check in the loop each score calling the function
  calification(grades[0])
print("-----------------------------------")
print("Physics Units Scores")
for grades in physics: # Check in the loop each score calling the function
  calification(grades[0])
