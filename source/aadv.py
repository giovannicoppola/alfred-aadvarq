#!/usr/bin/python3 
# giovanni
# Saturday, March 5, 2022, 8:46 AM
# Sunny ☀️   🌡️+30°F (feels +29°F, 51%) 🌬️↙4mph 🌒

import sys
import json
import os

MAXLENGTH = os.path.expanduser(os.getenv('MAXLENGTH', '0'))

def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

myLog = "".join([i for i in sys.stdin])

myTotal = len(myLog.split('\n')) - 1


result = {"items": []}

#log (myOut)

def main ():
    myCount = 0
    for T in myLog.splitlines():
        fullT = T
        lenT = len (T)
        if lenT > int(MAXLENGTH):
            T = T[1:50] + " ... " + T[80:len(T)]
        myCount += 1
        fileName= os.path.basename(T)
        result["items"].append({
                    "title": fileName,
                    "subtitle": str(myCount) + "/" + str(myTotal) + "-" + T,
                    "type": "file",
                    "icon": {"path": fullT, "type": "fileicon"},
                    "valid":'TRUE',
                            
                    "arg":fullT})
                

    print (json.dumps(result))

if __name__ == "__main__":
    main()