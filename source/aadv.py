#!/usr/bin/python3 
# giovanni
# Saturday, March 5, 2022, 8:46 AM
# Sunny ☀️   🌡️+30°F (feels +29°F, 51%) 🌬️↙4mph 🌒

import sys
import json
import os
import subprocess
#import time

MAXLENGTH = os.getenv('MAXLENGTH', '0')
SHOWLABELS = os.getenv('showLabelColors')

def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

myLog = "".join([i for i in sys.stdin])
myTotal = len(myLog.split('\n')) - 1


COLORS = {'Gray': '⚪', 'Green': '🟢', 'Purple': '🟣', 
          'Blue': '🔵', 'Yellow': '🟡', 'Red': '🔴', 'Orange': '🟠'}




def finder_tags(file_path):
    """Extract Finder tags of a given file in macOS"""
    output = subprocess.check_output(["mdls", "-name", "kMDItemUserTags", file_path]).strip()
    output = output.decode()
    tags = output.split("(")[1].split(")")[0].split(",")
    return [tag.strip() for tag in tags]


result = {"items": []}

#log (myOut)

def main ():
    myCount = 0
    
    for T in myLog.splitlines():
        fullT = T
        log (T)
    
        tagString = ''
        if (SHOWLABELS == "1"):
        
        
            tags = finder_tags(T)
            #tags = [sys.argv[2]]
            
            log (type(tags))

            if (tags):
                
                for myTag in tags:
                    if myTag in COLORS:
                        tagString = tagString + COLORS[myTag]
    
        lenT = len (T)
        if lenT > int(MAXLENGTH):
            T = T[1:50] + " ... " + T[80:len(T)]
        myCount += 1
        fileName= os.path.basename(T)
        result["items"].append({
                    "title": f"{fileName} {tagString}",
                    "subtitle": str(myCount) + "/" + str(myTotal) + "-" + T,
                    "type": "file",
                    "icon": {"path": fullT, "type": "fileicon"},
                    "valid":'TRUE',
                            
                    "arg":fullT})
                
    #startTS = sys.argv[3]
    
    #tts = time.time()
    #finalTime = tts - int(startTS)
    #log (f"================================Timestamp end of script (in sec): {finalTime:.2}")
    
    print (json.dumps(result))

if __name__ == "__main__":
    main()
