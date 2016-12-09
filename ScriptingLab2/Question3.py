#!/usr/bin/env python

###
#
# This script asks the user for a string, then for each vowel in the string
# it replaces that vowel with the next vowel in the sequence (A -> E, i -> o, u -> a).
#
###


# Make a string and set it to somebody's input.
strSentence = input("Write a beautiful passage you'd like to ruin.: ")

# Define the vowels in the english alphabet. ('Y' doesn't count)
listUpperVowels = ['A', 'E', 'I', 'O', 'U']
listLowerVowels = ['a', 'e', 'i', 'o', 'u']
indexUpper = 0
indexLower = 0

print("You asked for this.\n")

# Cycle throught the inputted string and set 'i' as each character.
for i in strSentence:
    # If i is in the list of uppercase vowels
    if st(i in listUpperVowels):
        # Set indexUpper to the index of (i + 1) in the list of uppercase vowels
        indexUpper = (listUpperVowels.index(i) + 1)
        # If i is an index higher than the length of the list, set it to 0
        if (indexUpper > 4): indexUpper = 0
        # Set i to the vowel at indexUpper in our list
        i = listUpperVowels[indexUpper]

    # Do the same as above but for lowercase vowels
    if (i in listLowerVowels):
        indexLower = (listLowerVowels.index(i) + 1)
        if (indexLower > 4): indexLower = 0
        i = listLowerVowels[indexLower]


    print(i, end="")

# Print a newline for more readability
input("\n\nPress Enter to Continue...")
