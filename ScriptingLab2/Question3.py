#!/usr/bin/env python

# Make a string and set it to somebody's input.
strSentence = input("Write a beautiful passage you'd like to ruin.: ")

# Define the vowels in the english alphabet. ('Y' doesn't count)
listVowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
listReplaceVowels = ['O', 'o', 'i', 'a', 'i', 'e', 'a', 'e']
indexReplaceVowels = 0

print("You asked for this.\n")

# Cycle throught the inputted string and set 'i' as each character.
for i in strSentence:
    # If i is in the vowels list, set it to the character at index 0 in the replace vowels list.
    if (i in listVowels):
        i = listReplaceVowels[indexReplaceVowels]
        # Increment the value that we index our 'listReplaceVowels' at by 1, if it is over 7 (The last value in the replacelist) set is back to 0
        indexReplaceVowels += 1
        if (indexReplaceVowels > 7): indexReplaceVowels = 0
    # Print i without being followed by a newline.
    print(i, end="")

# Print a newline for more readability
input("\n\nPress Enter to Continue...")
