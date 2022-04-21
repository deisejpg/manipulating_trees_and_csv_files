#!/usr/bin/python

''' 
    This script reads a phylogenetic tree in newick format, 
    gets tip names using a regular expression to find sample
    codes, and saves a single-column file with
    one sample code per line.

    Usage:
    python extract_tip_names.py

'''

import os
import re

#starting a file to write the tip names of our phylogenetic tree
treenames = open("./examples/names_on_the_tree.csv", "w")

matched = []
treefile = "./examples/concat.tre"
with open(treefile, "r") as tree:
    #looping over the tree and saving tip names to 'matched' list
    for line in tree:
        '''regex will match every time it reaches somethign that starts with
            A-Z and the '+' means it will add as many  letter until it reaches
            0-9 and A-B and it will keep adding numbers and A or B until it reaches
            a character that is different of those
            In the tree sample codes look like:
            "(JQ757046:0.0000014839," or "LP207928B:0.0021524120" or "(((ZSTU04567A:0.0249367663"
            it always starts with capital letter and finishes with numbers or capital A or B'''
        regex = r"(?:[/^A-Z_]+[0-9A-B]+)+"
        matches = re.finditer(regex, line)
        for matchNum, match in enumerate(matches):
            matched.append(match.group())

for i in matched:
    ''' 
    looping through each item of the list 'matched' and 
    writing a file with one column and one sample per line
    '''
    treenames.write(i+"\n")

new_line = "\n"
print(f"{new_line}There are {len(matched)} tips in the provided tree.")
print(f"Sample codes were saved in './examples/names_on_the_tree.csv.'{new_line}")