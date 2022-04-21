#!/usr/bin/python

''' 
    The goal of this script is to compare sample codes and sample 
    names of two datasets:
    Transcriptome or "all" (because this is the main dataset)
    Plastome or 'ptd'

    It uses pandas to read two files and to create a data frames.
    The first file will be the output from the previous step, in 
    which we extracted the names of a phylogenetic tree file.

    The second file has all the samples from the transcriptome dataset.
    This file has two columns, sample codes and species names in the
    format 'Family_Genus_species'.

    pd.merge() is used to gather information of overlapping and 
    non-overlapping samples.

    Some text is printed at the end with information about the number
    of overlapping samples to help confirming the results are correct.

    Usage:
    python compering_two_csv.py
'''

import os
import pandas as pd


#reading the file we just created as a data frame
#this should have 135 rows x 1 column
df_ptd = pd.read_csv("../examples/names_on_the_tree.csv", header=None)


#reading the file with the transcriptome dataset
#this file has sample code and sample names
#this should have 152 rows x 2 columns
df_all = pd.read_csv("../examples/renaming_samples.csv",sep='\t', engine='python')

#using merge() to get matching records
#there should be 67 matching samples
#to use "inner" below, I need to name the columns first
df_ptd.columns = ['samplecode']
df_all.columns = ['samplename','samplecode']
df_matching = df_ptd.merge(df_all, how='inner')
#If I don't want to name the columns I can use:
#df_matching = df_ptd.merge(df_all['samplecode'])
df_matching.to_csv('../examples/df_matching.csv')

#to get values only from the sample code column (column 2)
#df_all.iloc[:,1:]

#getting non-matching records
#there should be 69 non-matching samples
df_non_matching = df_ptd[~df_ptd.isin(df_all.to_dict('l')).all(1)]
df_non_matching.to_csv('../examples/df_non_matching.csv')

#selects all matches df_ptd and tag missing sample name info with "Nan"
#this will be helpful to detect which species names need to be updated
overlapped_sample_info_ptdbase = pd.merge(df_ptd,df_all, how='left')
overlapped_sample_info_ptdbase.to_csv('../examples/overlapped_sample_info_ptdbase.csv')

#the same as above but mapping on the transcriptome (df_all) samples
#uninformative in this case!
#overlapped_sample_info_allbase = pd.merge(df_ptd,df_all, how='right')
#overlapped_sample_info_allbase.to_csv('overlapped_sample_info_allbase.csv')

new_line = '\n'
print(f"{new_line}There are {len(overlapped_sample_info_ptdbase)} overlapping samples saved in: '../examples/overlapped_sample_info_allbase.csv'.{new_line}")

print(f"Of those, {len(df_matching)} have the same accession number in both datasets.")
print(f"Check it out in: '../examples/df_matching.csv'.{new_line}{new_line}")

print(f"There is a total of {len(df_non_matching)} samples that are either not represented in the plastome dataset {new_line}or have different accession numbers in both transcriptome and plastome datasets.")
print(f"Check it out in: '../examples/df_non_matching.csv'.{new_line}{new_line}")
