# Manipulating phylogenetic trees and csv files for tree annotation

This repo contains four scripts and examples for each script:

`I. extract_tip_names.py`

This script parses names of a phylogenetic tree using a regular expression. It outputs a single-column file with all the names that were parsed from the tree. The tree must be in newick format. The regular expression may need to be customized for different name formatting.  

Usage:  
```
python extract_tip_names.py
```

`II. comparing_two_csv.py`

This script reads two csv files, read them as pandas dataframes, compares names present in both columns and outputs files with overlapping/non-overlapping names.  

Usage:  
```
python comparing_two_csv.py
```

`III. renaming_trees.py`
	
This script takes two arguments, a csv file with two columns, listing sample codes and the respective species names; and a tree file that has identical sample codes as the tips of the tree. It saves a new file, also in newick format with new names.  

Usage:  
```
python renaming_trees.py treefile csvfile
```

`IV. extractTipNames_compareCSV.py`
	
This script runs the first two steps at once. It is still being developed to include functions to run each step and to include renaming the trees.  

Usage: 
```python
python extractTipNames_compareCSV.py
```
