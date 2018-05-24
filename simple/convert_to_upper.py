"""Uppercases a letter."""
s = input("Enter a letter: ")
s = s[0]
while not s.isalpha():
    print("Only letters allowed.")
    s = input("Please enter a letter: ")
    s = s[0]
print(s.upper())
