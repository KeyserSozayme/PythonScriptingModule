#!usr/bin/env python

Counter = 2

while (Counter < 100):
    
    # We will assume the 'Counter' is prime and our program will try to disprove that assumption.
    varIsCounterPrime = True
    
    # Set the variable 'i' to every number between 3 and the value of 'Counter' (But never equals 'Counter'),
    # Then divide 'Counter' by 'i' and if the remainder is ever 0 then it is not prime.
    for i in range (2, Counter):
    	if (Counter % i == 0): varIsCounterPrime = False
    
    # If 'Counter' stayed prime print the value of 'Counter'
    if (varIsCounterPrime): print(Counter)

    # Increment 'Counter' by 1 and start again.
    Counter += 1

input("\nPress Enter to Continue...")
