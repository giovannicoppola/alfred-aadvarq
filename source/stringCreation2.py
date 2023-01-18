#!/usr/bin/python3 

## STRING CREATION
# giovanni
# Saturday, March 5, 2022, 8:46 AM
# Sunny ☀️   🌡️+30°F (feels +29°F, 51%) 🌬️↙4mph 🌒


import sys

def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


myString =sys.argv[1]

myOutput = '-name '+myString

    
    
    



#log (myOutput)


print (myOutput)