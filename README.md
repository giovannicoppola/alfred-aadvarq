# alfred-aadvarq
 advanced finder tag search, in response to [this](https://www.alfredforum.com/topic/18041-advanced-search-using-tags-%C3%A0-la-finder/) Alfred forum discussion.  
![](aadvarq.gif "")
<a href="https://github.com/giovannicoppola/alfred-aadvarq/releases/latest/">
  
  <img alt="Downloads"
       src="https://img.shields.io/github/downloads/giovannicoppola/alfred-aadvarq/total?color=purple&label=Downloads"><br/>
</a>

# Usage
- search files based on Finder tags (case sensitive). 
- Boolean operators (`AND`, `OR`, `NOT`, case sensitive) accepted
- shorten the file path (helpful when very long and the actual file name is not visible). Set the max length in `Configure Workflow`
- general search (4-character min queries) with color-coded results based on Finder tags. May be slow for queries with many (>50) results.  


## Actions

- enter: open file
- ⌘ (CMD) + enter: show file in Finder
- ^ (CTRL) + enter: show complete path in large font


# Changelog
- 2023-01-19: version 0.0.5: Updated Boolean operators for `mdfind`
- 2023-01-19: version 0.0.4: added option to visualize color tags (in response to [this thread](https://www.alfredforum.com/topic/19532-colour-tag-in-search-results/)), added general search. 
- 2022-12-05: version 0.0.3 (Alfred 5)
- 2022-06-17: version 0.0.2 (adding icon for file type, thanks @vitorgalvao!)
- 2022-03-05: version 0.0.1 