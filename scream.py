import time
import sys
import os

hai=input(" Hey this is a simple CTF ")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
print(" Lets Do It... ")
slowprint("HINT : Base64 , Hexadecimal , Binary")
time.sleep(2)
os.system('clear')
print(hai)
slowprint("Use this link..     ")


print("Encoded : (aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2RyaXZlL2ZvbGRlcnMvMTNfeXlIZk10VDJ4U2c4TTYyVW1jcy1Za0tXamx0alF2P3VzcD1zaGFyaW5n)")
