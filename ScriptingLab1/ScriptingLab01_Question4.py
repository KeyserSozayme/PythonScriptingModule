#!/usr/bin/env python

# Define the amount of money we would like to break into coins.
# I am multiplying our values by 100 so we can use integers and avoid the innacuracies of using floats
valueStart = int(float(input("What is the Value of money you would like to break down into coins?: $")) * 100)
valueDecrimented = valueStart

# Define the values of canadian coins. (x100)
valueQuarter, valueDime, valueNickel, valuePenny = 25, 10, 5, 1

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
    "\nStarting money:    $"  + str(float(valueStart) / 100) +
    "\nNumber of Quarters: "  + str(numQuarters) +
    "\nNumber of Dimes:    "  + str(numDimes) +
    "\nNumber of Nickels:  "  + str(numNickels) +
    "\nNumber of Pennies:  "  + str(numPennies)
    )

# Essentially just the python equivalent of "PAUSE" for Batch
input("\nPress enter to continue...")
