# Define the values of canadian coins.
valueQuarter = 0.25
valueDime = 0.10
valueNickel = 0.05
valuePenny = 0.01

# Define the 'default' number of coins that are in our starting value.
numQuarters = 0
numDimes = 0
numNickels = 0
numPennies = 0

# Define the amount of money we would like to break into coins.
valueStart = 3.73
valueDecrimented = valueStart

# Determine the amount of Quarters and subtract that from our starting total.
numQuarters = valueDecrimented // valueQuarter
valueDecrimented -= (numQuarters * valueQuarter)

# Do the same with Dimes.
numDimes = valueDecrimented // valueDime
valueDecrimented -= (numDimes * valueDime)

# Do the same with Nickels.
numNickel = valueDecrimented // valueNickel
valueDecrimented -= (numNickels * valueNickel)

# Do the same with Pennies.
numPennies = valueDecrimented // valuePenny
valueDecrimented -= (numPennies * valuePenny)

print(valueDecrimented,
      valueStart,
      numQuarters,
      numDimes,
      numNickels,
      numPennies)





