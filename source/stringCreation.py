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

myList=myString.split()

#log (len(myList))

myFirst = myList[0]
myOutput = 'tag:'+myFirst

if len(myList)>1:
 
    
    for ele in myList[1:]:
        if ele in ['AND','OR','NOT']:
            myOutput = myOutput + " " + ele        
        else:
            myOutput = myOutput + " tag:" + ele        
        
    
    
    



#log (myOutput)


print (myOutput)