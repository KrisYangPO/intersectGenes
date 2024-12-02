#!/usr/bin/env python3
# multiple selection of DEGs 
# create: 2024/7/20

from Merge_filterDEGs import *
from Merge_multiMerge import *
from Merge_formGeneDict import *


# In[] read input information dictionary and decide which algorithms should be performed.
# output gene_dicts and all cols:

def gainInput(input_dict): 
    gene_dicts = []
    all_cols = []
    outname = []
    

    # read DESeq2 output table file:
    if input_dict["mode"] == "DEG":   
        
        # specifically input DESeq2 output table.
        # read files and create their gene_dictionaries
        df, col, filename = readDataframe(input_dict["DESeq_file"])
        df = multiselect_DEG(df, input_dict["select"], input_dict["value"])
        gene_dict = createGeneDict(df, g_index = input_dict["DESeq_index"])
        
        # append to a list 
        gene_dicts.append(gene_dict)
        all_cols.append(col)
        outname.append(filename)

    
    # read other files:
    for file in input_dict["file_list"]:
        
        # read files and create their gene_dictionaries
        df, col, filename = readDataframe(file)
        gene_dict = createGeneDict(df, g_index = input_dict["index"])

        # append to a list 
        gene_dicts.append(gene_dict)
        all_cols.append(col)
        outname.append(filename)
            

    # check
    if len(gene_dicts) != len(all_cols): 
        print("packInput: Missing columns or missing file!")
        return

    return gene_dicts, all_cols, outname


