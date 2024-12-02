#!/usr/bin/env python3
# merge_dict two geneData_Dict
# create: 2024/7/10
# version: 3

"""
version update:
1. OverlappingGeneList():
    create a overlapping gene reference list based on a list containing all gene_dictionaries.

2. merge2dict:
    Same as the previous version that merge only two gene_dictionaries by finding identical geneID. 

3. mergeDict:
    extract target genes from a gene_dictionary based on the overlapping gene reference
    derived from OverlappingGeneList() function.

4. mergeMultiDict:
    compare several gene_dictionaries to overlapping gene reference,
    and merge their information into a list based on the identical gene ID.
    
"""


# In[] find overlap genes
# Input a list containing several dictionaries. 

def overlappingGeneList(dict_list):

    # gather all gene IDs from a list:
    All_gene = []
    gene_count = 0
    for i in range(0, len(dict_list)):

        All_gene += list(dict_list[i].keys())
        gene_count += len(list(dict_list[i].keys()))    

    
    # check gene number consistency:
    if gene_count != len(All_gene):
        print("MultiMerge: Total number of genes from dictionaries is not equal to All_gene.")
        return
    else: 
        print("MultiMerge: Total genes number: ", gene_count, "\n", "The length of Gene list: ", len(All_gene))


    # find overlapping genes in a gene ID list:
    overlap={}
    for i in range(0, len(All_gene)):
        
        # count how many times a gene ID appeared in gene list:
        if All_gene[i] not in overlap:
            overlap[All_gene[i]] = 1
        else:
            overlap[All_gene[i]] += 1

    """
    To find genes that present in all dictionaries, determine whether
    their repetitive number (rep) is equivalent to number of input dictionaries.
    if the repeat number of a gene is equal to the number of input dictionaries,
    suggesting that this gene present in all dictionaries (if rep == len(dict_list)). 
    """
    overlappingGene = [gene for gene, rep in overlap.items() if rep == len(dict_list)]
    print("MultiMerge: Total overlapped genes number: ", len(overlappingGene))
    return overlappingGene



# In[] start to merge GeneID_dictionaries based on same Gene IDs:
# input a single dictionary and overlapping gene list.
# simply find the co-target genes in a gene_dict.

def mergeDict(gene_dict, overlappingGene):
    match = {} 
    unmatch = {}

    # using .items() to gain both key and value at the same time.
    for gene, info in gene_dict.items():

        # if gene match gene list, add gene's information:
        if gene in overlappingGene:
            match[gene] = info
        
        else: unmatch[gene] = info

    # check miss match
    if (len(match.keys()) + len(unmatch.keys())) != len(gene_dict.keys()):
        print("MultiMerge: There are missing values in gene_dict and matched genes. ")
        return      

    return match, unmatch



# In[] merge two gene_dicts based on two gene dictionaries
# input two geneID_dictionaries, determine the overlapping genes from their keys

def merge2Dict(df1_dict, df2_dict):
    
    match = {}
    unmtach = {}

    # keys represent gene ID
    for gene in df1_dict.keys():
        
        # df2_dict.keys(): list contains df2_dict ID
        # merge_dict gene informations if df2_dict overlaps cluster gene:
        # using "+" assemble two values into a match dict value
        if gene in df2_dict.keys():
            match[gene] = df1_dict[gene] + df2_dict[gene]

        else: unmtach[gene] = df1_dict[gene]


    # check whether there is a missing gene: 
    if (len(match) + len(unmtach)) != len(df1_dict):
        print("MultiMerge: Miss some genes after matching df1 and df2's genes.")
        return

    return match, unmtach



# In[] search overlapping genes from several gene_dict by comparing overlapping gene list:
# Input list may contain several gene_dictionaries, only genes overlap in all dictionaries will be selected.
# unmatch geneID will be output as a unmatch gene list (dictionary with on key-value) rather than a dataframe data. 

def mergeMultiDict(gene_dict_list, overlappingGene):
    
    match = {}
    unmatch = {"unmatch_gene": []}

    # invoke each gene_dict
    for dict in gene_dict_list: 
        
        # determine whether gene ID in overlapping_gene list:
        for geneID, info in dict.items():
            
            # find overlapping genes from the gene_dict by reference list.
            if geneID in overlappingGene:
                
                # If a geneID-infor has been created by previous gene_dict
                # append the value from other gene_dict in the same geneID-infor dictionary.
                if geneID not in match:
                    match[geneID] = info
                else: match[geneID] += info

            # unmatch gene list 
            else: 
                unmatch["unmatch_gene"].append(geneID)
    

    # check whether there is an erroneous matching:
    for match_gene, info in match.items():
        if match_gene in unmatch.values():
            print("MultiMerge: Gene: ", match_gene, " is also present in unmatch group.")
            return


    return match, unmatch

