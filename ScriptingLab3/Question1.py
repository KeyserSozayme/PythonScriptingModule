import os

# THIS SCRIPT MUST BE RUN FROM AND ADMINISTRATIVE CMD PROMPT TO WORK!!!
# If it is run form IDLE this script will not work!

while True:
    # Set 'username' to the input of the following prompt.
    username = input("Enter a user you'd like to add to your current system.: ")
    # Set that user's password
    password = input("Enter the password for " + username + ": ")

    # Using cmd, add the specified user with the specified password
    os.system("NET USER " + username + " " + password + " /ADD &&")

    if ((input("Would you like to add anothe user? ('Y', or 'N')")) != 'y'):
        break
    
print("Done!")
