# Import the OS Library
import os

# Set a list of pingable addresses
pingAddresses = ['127.0.0.1','8.8.8.8','8.8.4.4','www.google.com']

# Cycle through the list and set 'address' as each address in our list.
for address in pingAddresses:
    # Ping each address.
    # Also pause after each ping so we can actually read the output.
    os.system("ping " + address + " && pause")
    
# Print 'Done' and pause when finished
input("Done!\nPress Enter to continue...")
