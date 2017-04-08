#!/usr/bin/env python

# Create Divisor and Dividend Variables
varDivisor = 8
varDividend = int(input("Enter any Integer other than zero to see if it is a multiple of "+ str(varDivisor) + ": "))

# Modulus our variables and if the output is 0 that means there is no remainder after dividing our Dividend and Divisor.
if ((varDividend % varDivisor) == 0):
    print("\nSuccess!\nThe number: " + str(varDividend) + " is a multiple of: " + str(varDivisor))
else:
    print("\nFailure.\nThe number: " + str(varDividend) + " is not a multiple of: " + str(varDivisor))
    
# Helpful PAUSE for when running scripts from CLI
input("\nPress Enter to continue...")
