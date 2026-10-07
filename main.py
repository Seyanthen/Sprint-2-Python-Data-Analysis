"""
So this is actually a string
But it will be ignored by the interpreter
Because it is not assigned to a variable.
Its a weird comment format
"""

# Learning IO stream
print("Hello, World!")

#name = input("What is your name? ")
#print(f"Hello, {name}! Welcome to the program.")

print("Check line 7 for an example of semicolon use.", end=" ") ; print("It's not common in Python")

print("There can be numbers like", 5, "in a print statement")

# Learning Python Indentation and Loops
x = 5
print (f"x is {x}")

while x > 2:
    print(f"{x} is greater than 2")
    x = x - 1

print(f"Now x is {x}")

# Looping through a string as an array
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")