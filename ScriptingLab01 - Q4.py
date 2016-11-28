#!/usr/bin/env python
from decimal import getcontext, Decimal

#
getcontext().prec = 2

# Define the amount of money we would like to break into coins.
valueStart = Decimal(input("What is the Value of money you would like to break down into coins?: $"))
valueDecrimented = valueStart

# Define the values of canadian coins.
valueQuarter, valueDime, valueNickel, valuePenny = Decimal(0.25), Decimal(0.10), Decimal(0.05), Decimal(0.01)

# Define the 'default' number of coins that are in our starting value.
numQuarters, numDimes, numNickels, numPennies = Decimal(0), Decimal(0), Decimal(0), Decimal(0)

print(valueDecrimented)

# Determine the amount of Quarters and subtract that from our starting total.
numQuarters = (valueDecrimented // valueQuarter)
valueDecrimented -= (numQuarters * valueQuarter)
print(valueDecrimented)

# Determine the amount of Dimes that are left after subtracting the value of all the quarters.
numDimes = (valueDecrimented // valueDime)
valueDecrimented -= (numDimes * valueDime)
print(valueDecrimented)

# Do the same with Nickels.
numNickel = (valueDecrimented // valueNickel)
valueDecrimented -= (numNickels * valueNickel)
print(valueDecrimented)

# Do the same with Pennies.
numPennies = (valueDecrimented // valuePenny)
valueDecrimented -= (numPennies * valuePenny)
print(valueDecrimented)

print("Starting Money: $"+ str(valueStart)+"\n"+
      "# of Quarters: "+ str(numQuarters)+"\n"+
      "# of Dimaes: "+ str(numDimes)+"\n"+
      "# of Nickels: "+ str(numNickels)+"\n"+
      "# of Pennies: "+ str(numPennies))
