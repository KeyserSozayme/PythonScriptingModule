# Import some libraries that help us retrieve system info
import platform, time, os

# Print some information the our platform library returns
print(
    "\nSome Information about your system is...\n"
    "\nCPU Archetecture....." + platform.machine() +
    "\nOperating System....." + platform.platform()  +
    "\nOS Version..........." + platform.version() +
    "\nProcessor............" + platform.processor()
    )

# Run a loop ten times, that will sleep for 1 second between each call
print("\nYour CPU Usage over the next ten seconds is as follows...\n")
for i in range(0, 10):

    
    # Print our Current CPU Load percentage,
    # 
    # This would be a lot easier if i would be able to download extra
    # libraries over the internet, but then the code would only work
    # on my machine, therefore I have to use this bodge for it to work
    # on other computers as well.
    
    print(str(os.popen("WMIC CPU GET LoadPercentage ").read()))
    
    time.sleep(1)
    i = i + 1

# Print 'Done' and pause when finished
input("Done!\nPress Enter to continue...")
