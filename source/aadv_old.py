#!/usr/bin/python3 
# giovanni
# Saturday, March 5, 2022, 8:46 AM
# Sunny ☀️   🌡️+30°F (feels +29°F, 51%) 🌬️↙4mph 🌒

import sys
import json
import os
import subprocess
import time
 


MAXLENGTH = os.getenv('MAXLENGTH', '0')
SHOWLABELS = os.getenv('showLabelColors')

def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

myLog = "".join([i for i in sys.argv[1]])
myTotal = len(myLog.split('\n')) - 1

COLORS = {'Gray': '⚪', 'Green': '🟢', 'Purple': '🟣', 
          'Blue': '🔵', 'Yellow': '🟡', 'Red': '🔴', 'Orange': '🟠'}




def finder_tags(file_path):
    """Extract Finder tags of a given file in macOS"""
    output = subprocess.check_output(["mdls", "-name", "kMDItemUserTags", file_path]).strip()
    output = output.decode()
    tags = output.split("(")[1].split(")")[0].split(",")
    return [tag.strip() for tag in tags]


def get_file_tags(file_path):
    # Use mdfind to search for the file and retrieve its tags
    result = subprocess.run(["mdfind", "-onlyin", file_path, "kMDItemUserTags"], capture_output=True)

    # Extract the tags from the output
    tags = result.stdout.decode().strip().split(",")

    return tags

result = {"items": []}

#log (myOut)

def main ():
    myCount = 0
    for T in myLog.splitlines():
        fullT = T
        #log (T)
    
        tagString = ''
        if (SHOWLABELS == "1"):
        
        
            #tags = finder_tags(T)
            tags = [sys.argv[2]]
            #log (f"TAAAAAAGS: {tags}")
            #log (type(tags))

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
                
    startTS = [sys.argv[3]][0]
    
    tts = time.time()
    finalTime = tts - int(startTS)
    log (f"================================Timestamp end of script (in sec): {finalTime:.2}")
    print (json.dumps(result))
    
    
if __name__ == "__main__":
    main()



"""
SECOND VERSION
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
myQuery="$1"
myTS=$(date +%s)
#>&2 echo $myTS

if [[ ${#myQuery} -gt 3 ]]
then
	myFiles=$(mdfind "kMDItemFSName == '*$myQuery*'" -onlyin ~/) 
	# Define an empty array to store the results
	metadata_array=()

	for file_path in "${myFiles[@]}"
	do
	  # Use mdls to retrieve the metadata of the file
	  metadata=$(mdls -name kMDItemUserTags "$file_path")
	  # Append the metadata to the array
	  metadata_array+=("$metadata")
	done
	python3 aadv.py "$myFiles" "$metadata_array" "$myTS"

else
cat << EOB
	{"items": [
		{
			"title": "❗Enter 4 characters at least",
			"subtitle": "length: ${#myQuery} (${myQuery})"

			}
]}
EOB
fi


### RELEASED VERSION
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
myQuery="$1"


if [[ ${#myQuery} -gt 3 ]]
then
	mdfind "kMDItemFSName == '*$myQuery*'" -onlyin ~/ | python3 aadv.py
else
cat << EOB
	{"items": [
		{
			"title": "❗Enter 4 characters at least",
			"subtitle": "length: ${#myQuery} (${myQuery})"

			}
]}
EOB
fi




MOST RECENT
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
myQuery="$1"


if [[ ${#myQuery} -gt 3 ]]
then
	if [[ ${#myQuery} -gt 3 ]]
then
	# Use the -0 option to separate file names with a null character
    IFS=$'\n'
    while read -r -d '' file; do
    # Append the file name to the array
    files+=("$file")
    done < <(mdfind "kMDItemDisplayName == '*$myQuery*'c" -0 -onlyin ~/)


	for file_path in "${files[@]}"
    
	do
	  #echo "Current path: $file_path"
      # Use mdls to retrieve the metadata of the file
	  tags=$(mdls -name kMDItemUserTags "$file_path")
      #echo "current tags before parsing: $tags"
      tags=$(mdls -name kMDItemUserTags "$file_path" | sed 's/kMDItemUserTags = (//g' | sed 's/)//g' | tr -d ' ' | tr -d '\n')
      #echo "parsed tags: $tags"
        
      # Append the tags to the array
      tags_array+=("$tags")
	done

    #printf '%s\n' "${tags_array[@]}"
fi


	python3 aadv.py "$files" "$tags_array"

else
cat << EOB
	{"items": [
		{
			"title": "❗Enter 4 characters at least",
			"subtitle": "length: ${#myQuery} (${myQuery})"

			}
]}
EOB
fi





CLEANED UP
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
myQuery="$1"


if [[ ${#myQuery} -gt 3 ]]
then
	if [[ ${#myQuery} -gt 3 ]]
then
	# Use the -0 option to separate file names with a null character
    IFS=$'\n'
    while read -r -d '' file; do
    # Append the file name to the array
    files+=("$file")
    done < <(mdfind "kMDItemDisplayName == '*$myQuery*'c" -0 -onlyin ~/)


	for file_path in "${files[@]}"
    
	do
	  
      # Use mdls to retrieve the metadata of the file
	  # then parse the output
      tags=$(mdls -name kMDItemUserTags "$file_path" | sed 's/kMDItemUserTags = (//g' | sed 's/)//g' | tr -d ' ' | tr -d '\n')
      
        
      # Append the tags to the array
      tags_array+=("$tags")
	done

    
fi


	python3 aadv.py "$files" "$tags_array"

else
cat << EOB
	{"items": [
		{
			"title": "❗Enter 4 characters at least",
			"subtitle": "length: ${#myQuery} (${myQuery})"

			}
]}
EOB
fi


"""
"""