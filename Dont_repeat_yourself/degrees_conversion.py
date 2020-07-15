# Luis Fernando Koh Avila
# Data 2 B

# CODE AFTER OPTIMIZATION

# Function that converts Celsius to Fahrenheit and Kelvin
def cel_to_fk(celsius):
  fahrenheit = celsius * ( 9 / 5 ) + 32
  kelvin = celsius + 273
  print(f"""
  Temperature in celsius: {celsius}
  Converted to kelvin: {kelvin}
  Converted to fahrenheit: {fahrenheit}
  """)

# Function that converts Kelvin to Celsius and Fahrenheit
def kel_to_cf(kelvin):
  celsius = kelvin - 273
  fahrenheit = celsius * ( 9 / 5 ) + 32
  print (f"""
  Temperature in kelvin: {kelvin}
  Converted to celsius: {celsius}
  Converted to fahrenheit: {fahrenheit}
  """)

# Function that converts Fahrenheit to Celsius and Kelvin
def fahr_to_cf(fahrenheit):
  celsius = (5 * (fahrenheit - 32)) / 9
  kelvin = celsius +273
  print (f"""
  Temperature in fahrenheit: {fahrenheit}
  Converted to celsius: {celsius}
  Converted to kelvin: {kelvin}
  """)

# Degrees to convert
celsius = [[60],[90]]
fahrenheit = [[32],[40]]
kelvin = [[60],[40]]

# For to call the function and convert the degrees
for degrees in celsius:
  cel_to_fk(degrees[0]) # Check in the loop each degree and calling the function
print("----------------------------------")
for degrees in fahrenheit:
  fahr_to_cf(degrees[0]) # Check in the loop each degree and calling the function
print("----------------------------------")
for degrees in kelvin:
  kel_to_cf(degrees[0]) # Check in the loop each degree and calling the function
