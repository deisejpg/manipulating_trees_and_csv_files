#!/usr/bin/python

'''

    This script renames tips of a phylogenetic tree in newick format.

    It takes a .tre/.nwk file and a .csv file that has two columns (species_code, 
    species_names).

    Usage:
    python renaming_trees.py treefile.tre samplesnames.csv
    python renaming_trees.py ./examples/concat.tre ./examples/renaming_ptd_samples_fullnames.csv

    Note:
    - make sure the sample_code in csv is identical to the sample_code in the treefile
    - the tree won't open in figtree if there are more than one identical species names

    To improve:
    - parse tip names and find a way to avoid using replace()
    - Update code to add a function to rename the tips of a tree
'''


import os
import fnmatch
import csv
from sys import argv

'''checks if the arguments were correctly passed'''
if __name__ == '__main__':
    if len(argv) != 3:
        print('It seems that you forgot something! You need:')
        print('python renaming_trees.py treefile.tre samplesnames.csv')
        print("Check the './examples' directory for examples of file formats")
        exit(1)
tree   = argv[1]
csv    = argv[2] 

''' - opening the file with old and new names - csv file
    - adding the first column as keys and the second column as values - names dictionary
    - for some reason I still could not figure I got utf-8-sig on my code
        it didn't work to revome it with 'encoding' argument in open() so
        I used '.strip()' to remove the BOM'''
names = {} 
#with open("../examples/renaming_ptd_samples.csv") as columns: 
with open(csv, "r") as columns:
    for line in columns:  
        line = line.strip('\ufeff').strip("\n").split(",")  
        names[line[0]] = line[1]                                 


''' - opening the file with the tree in newick format - infile object
    - opening a file to write the renamed tree - retree object
    - reading the original tree and using the dictionary to rename the tips as a list - lines
    - looping through the 'lines' list to save the renamed tree as a new file'''
lines = [] 
#with open("../examples/concat.tre", "rt") as infile: 
with open(tree, "rt") as infile:
    with open("../examples/concat.renamed.tre", "wt") as retree: 
        for line in infile:             
            for key,value in names.items(): 
                if key in line: 
                    line = line.replace(key,value, 1) 
            lines.append(line)     
        for i in lines:
            retree.write(i)

#printing some information about what was done and where the output is
print()
print(f"Tips of {tree} were renamed and the new tree was saved at '../examples/concat.renamed.tre'")
print()
print("Done!")