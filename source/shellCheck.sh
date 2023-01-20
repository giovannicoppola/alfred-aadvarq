myQuery="sand"



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
	  echo "Current path: $file_path"
      # Use mdls to retrieve the metadata of the file
	  tags=$(mdls -name kMDItemUserTags "$file_path")
      echo "current tags before parsing: $tags"
      tags=$(mdls -name kMDItemUserTags "$file_path" | sed 's/kMDItemUserTags = (//g' | sed 's/)//g' | tr -d ' ' | tr -d '\n')
      echo "parsed tags: $tags"
        
      # Append the tags to the array
      tags_array+=("$tags")
	done

    printf '%s\n' "${tags_array[@]}"
fi

