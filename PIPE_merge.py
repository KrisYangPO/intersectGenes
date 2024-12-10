#!/usr/bin/env python3
# hypergeometric: find overlapped genes
# version1: 2024/7/20

import pandas as pd
from glob import glob
from Merge_filterDEGs import *
from Merge_multiMerge import *
from Merge_formGeneDict import *
from Merge_packInput import *


# In[] perform DEGs comparison
# Find overlapping genes from a single cluster data and DEGs.
# input a list of cluster data, and compare each data with DESeq table to find overlapping genes.
# output matched overlapping gene dataframe derived after the comparison of each cluster data and DEGs. 

def compare_DEGsMerge(input_dict):
    # Steps:
    # 1. input files summarizing (gainInput())
    # 2. merge two dictionary using merge2Dict()
    # 3. output files

    # read file and create its gene_dictionary:
    # If it is a DEG comparison, the DEGs gene dict will be place at first index of these three outputs. 
    gene_dicts, cols, outname = gainInput(input_dict)
    print("1. GeneID_dicts have been created.")


    # merge each gene_dict with DESeq2 output table:
    match_dict = []
    unmatch_dict = []

    if input_dict["mode"] == "DEG":
        # range start from 1 to exclude DESeq Gene_dict (where the information is placed at index 0)
        for i in range(1, len(gene_dicts)):
            match, unmatch = merge2Dict(gene_dicts[0], gene_dicts[i])
            match_dict.append(match)
            unmatch_dict.append(unmatch)

    else:
        print("Your mode is: ", input["mode"], "\n","This function is required for DEGs comparison mode; use compare_mergeMulti() instead.")
        return


    # check length
    if len(match_dict) != len(unmatch_dict):
        print("EXE: Missing value after MERGE.")
        return
    
    print("2. Files merging completed.")
    
    # output data
    # "+1" from the cols and the outname is used to exclude DESeq table's information
    for i in range(0, len(match_dict)):
        
        # create dataframe
        match_df = pd.DataFrame(match_dict[i], index = cols[0] + cols[i+1]).T
        unmatch_df = pd.DataFrame(unmatch_dict[i], index = cols[0]).T

        # output match data
        match_df.to_csv(input_dict["outputpath"] + "MERGE_DEGs_" + outname[i+1]+ ".bed", sep = "\t")
        unmatch_df.to_csv(input_dict["outputpath"] + "unmatch_MERGE_DEGs_" + outname[i+1]+ ".bed", sep = "\t")

    print("Finished!!")

    return match_df, unmatch_df



# In[] mergeReplicates & DEGs
# find overlapping genes from clusters replicates and DEGs.

def compare_mergeMulti(input_dict):
    
    # read file and create its gene_dictionary:
    # If it is a DEG comparison, the DEGs gene dict will be place at first index of these three outputs. 
    gene_dicts, cols, outname = gainInput(input_dict)
    print("1. Data has received.")

    # merge each gene_dict with DESeq2 output table:
    # perform extracting overlapping genes from all clusters.
    # perform multi-Gene dictionaries merging based on overlapping gene reference.

    match_dict, unmatch_dict = mergeMultiDict(gene_dicts, overlappingGeneList(gene_dicts))
    print("2. Overlapping genes and their information has been stored in match.")


    # output part:
    # summarize col name from each input data from function: gainInput.
    out_cols = [col for file_col in cols for col in file_col]

    # create pd.dataframe
    match_df = pd.DataFrame(match_dict, index = out_cols).T
    unmatch_df = pd.DataFrame(unmatch_dict)
    print("3. Dataframes are created.")

    print(match_df.head(5))

    # output name:
    match_name = (input_dict["outputpath"] + input_dict["outputname"])
    unmatch_name = (input_dict["outputpath"] + "unmatch_Genelist_" + input_dict["outputname"])
    
    match_df.to_csv(match_name, sep = "\t", index = False)
    unmatch_df.to_csv(unmatch_name, sep = "\t", index = False)
    
    print("4. Output tables have been saved.")
    print("Program completed.")

    return match_df, unmatch_df


