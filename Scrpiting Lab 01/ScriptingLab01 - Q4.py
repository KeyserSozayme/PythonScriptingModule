#!/usr/bin/env python

# Define the amount of money we would like to break into coins.
valueStart = float(input("What is the Value of money you would like to break down into coins?: $"))
valueDecrimented = valueStart

# Define the values of canadian coins.
valueQuarter, valueDime, valueNickel, valuePenny = 0.25, 0.10, 0.05, 0.01

# Define the 'default' number of coins that are in our starting value.
numQuarters, numDimes, numNickels, numPennies = 0, 0, 0, 0

# Determine the amount of Quarters and subtract that from our starting total.
numQuarters = (valueDecrimented // valueQuarter)
valueDecrimented -= (numQuarters * valueQuarter)

# Determine the amount of Dimes that are left after subtracting the value of all the quarters.
numDimes = (valueDecrimented // valueDime)
valueDecrimented -= (numDimes * valueDime)

# Do the same with Nickels.
numNickels = (valueDecrimented // valueNickel)
valueDecrimented -= (numNickels * valueNickel)

# Do the same with Pennies.
numPennies = (valueDecrimented // valuePenny)
valueDecrimented -= (numPennies * valuePenny)

# Output the results of the program
print(
    "\nStarting money:    $"  + str(valueStart) +
    "\nNumber of Quarters: "  + str(numQuarters) +
    "\nNumber of Dimes:    "  + str(numDimes) +
    "\nNumber of Nickels:  "  + str(numNickels) +
    "\nNumber of Pennies:  "  + str(numPennies)
    )

# Essentially just the python equivalent of "PAUSE" for Batch
input("\nPress enter to continue...")
