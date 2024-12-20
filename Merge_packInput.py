#!/usr/bin/env python3
# multiple selection of DEGs 
# create: 2024/12/16

from Merge_filterDEGs_v2 import *
from Merge_multiMerge import *
from Merge_formGeneDict import *
import pandas as pd


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
        df, report_dict = multiselect_DEG_advanced2(df, input_dict["DEG_selection"])
        col.append("indicator")

        # write a report file:
        DEGs_report = pd.DataFrame(report_dict)
        print(DEGs_report)
        DEGs_report.to_excel("DEGs_select_report.xlsx")

        # Add a column name for DEG indicator at the end of the selected DESeq2 table.
        gene_dict = createGeneDict(df, g_index = input_dict["DESeq_index"])
        
        # append to a list 
        gene_dicts.append(gene_dict)
        all_cols.append(col)
        outname.append(filename)

    
    # read other files:
    for file in input_dict["file_list"]:
        
        # read files and create their gene_dictionaries
        df, col, filename = readDataframe(file)
        gene_dict = createGeneDict(df, g_index = input_dict["index"][0])

        # append to a list 
        gene_dicts.append(gene_dict)
        all_cols.append(col)
        outname.append(filename)
            

    # check
    if len(gene_dicts) != len(all_cols): 
        print("packInput: Missing columns or missing file!")
        return

    return gene_dicts, all_cols, outname


