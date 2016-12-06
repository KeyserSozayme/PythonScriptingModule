#!/usr/bin/env python
# Import the 'randrange' function fromm the 'random' library
from random import randrange


# Make a string and set it to somebody's input.
strSentence = input("Write a beautiful passage you'd like to ruin.: ")

# Define the vowels in the english alphabet. ('Y' doesn't count)
listVowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print("You asked for this.\n")

# Cycle throught the inputted string and set 'i' as each character.
for i in strSentence:
    # If 'i' is in the list of vowels, set it as a random vowel from the list of vowels.
    # Then print i with the end character an empty string.
    if (i in listVowels):
        i = listVowels[randrange(0, 9)]
    print(i, end="")

# Print a newline for more readability
input("\n\nPress Enter to Continue...")
