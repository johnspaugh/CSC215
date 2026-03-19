
# start up page to call on other pages maybe
#first up is to call on the data set hosted in google drive

import time
import subprocess
import sys

def callDataSet():
    print("starting the function call DataSet for debugging")


try:

    print("hello World");

    # Runs script_b and captures its printed output
    # result = subprocess.run([sys.executable, "script_b.py"], capture_output=True, text=True)
    # value = result.stdout.strip()
    # print(f"Captured: {value}")
    # Note: Use capture_output=True and text=True to get the output as a string instead of bytes.
    # Verification: You can check result.returncode to see if the script finished successfully (0 usually means success).

# to catch errors likely from socket trying to setup
except Exception as e:
    print(f"Server error: {e}")
    
# #4 handling debugging to insure it closes
# except KeyboardInterrupt:
#     print("Caught keyboard interrupt, exiting")
#     # s.close()
#     # print("Server closed")
#     # sys.exit(0)
# finally: