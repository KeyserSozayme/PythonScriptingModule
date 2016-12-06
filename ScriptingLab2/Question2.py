#!/usr/bin/env python

# Set our 'Default' running total.
varRunningTotal = 0

# As long as our total is less than, or equal to 1000, keep prompting us to add to that total.
while (varRunningTotal <= 1000):
    # Print current total and ask us to add to it.
    varRunningTotal += int(input("The current total is " + str(varRunningTotal) + ", enter an integer to add to that total.: "))
    
# The while loop has been broken, this just tells us what the total was when we left the loop.
input("\nThe Total was " + str(varRunningTotal) + ",\nPress Enter to Continue")
