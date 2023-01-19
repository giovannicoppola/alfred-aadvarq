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
myOutput = f'kMDItemUserTags == "{myFirst}"'

if len(myList)>1:
 
    
    for ele in myList[1:]:
        if ele.strip() == 'AND':
            myOutput = f"{myOutput} &&"
        elif ele.strip() == 'OR':
            myOutput = f"{myOutput} ||"
        elif ele.strip() == 'NOT':
            myOutput = f"{myOutput} && !"
        
        else:
            myOutput = myOutput + " kMDItemUserTags ==" + ele        
        

    
    
    



log (myOutput)


print (myOutput)