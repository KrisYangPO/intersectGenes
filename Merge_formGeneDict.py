#!/usr/bin/env python3
# create a geneID_dictionary data in a function 
# create: 2024/7/10

import pandas as pd

# In[] read files:
def readDataframe(filename):

    try:
        # determine the input format:
        if ".xlsx" in filename:
            df = pd.read_excel(filename)
            filename = filename.replace(".xlsx","")

        elif ".bed" or ".txt" in filename:
            df = pd.read_csv(filename, sep = "\t")
            filename = filename.replace(".bed","").replace(".txt","")

        else:
            print("readDATA: ", filename, " is not a dataframe or Tab-splited table.")


        # design output column name with fileanme in column 1:
        df_cols = list(df.columns)
        df_cols[0] = df_cols[0] + "; filename: " + filename


        print("readDATA: file name: ", filename)
        return df, df_cols, filename
    
    
    except TypeError:
        print("Unkknown file type.")
        return


# In[]
# create GeneList data 
# create: 2024/7/10
'''
Generate a dictionary with gene IDs stored as keys and their values containing
gene's information, such as differential expression (DESeq2) 
and differential coverage (heatmap cluster).

df: target dataframe, creating their (geneID:column) information based on Gene ID index.
g_index: indicates the the column index that store gene ID.

'''

def createGeneDict(df, g_index):
    dft = (df.T)

    # check transposing:
    if len(dft.iloc[0,:]) != len(df.iloc[:,0]):
        print("Create Dict: Missing rows or erroneous column number after transposing!")
        return

    print(dft.head(5))
    print(df.head(5))


    # create dictionary data based on gene list:
    # genedata: contains gene's information
    # gene: gene ID from genedata list (row: g_index indicates Gene ID column)
    # len(df) == row length
    gene_Datadict={}
    for i in range(0, len(df)):
        genedata = list(dft.iloc[:,i])
        gene = genedata[g_index].upper()

        # avoid repetitive genes
        if gene not in gene_Datadict:
            gene_Datadict[gene] = genedata
        else: 
            print("Create Dict: Gene: ",gene, " has been added into gene list.") 
            continue

        # check whether there is a key:information miss-match:
        if gene != gene_Datadict[gene][g_index].upper():
            print("Create Dict: Gene ID: ",gene, " was not match to its information (values)")
            return 


    # check whether there is a missing value:
    if len(gene_Datadict) != len(dft.iloc[0,:]):
        print("Create Dict: Missing Value after creating geneData_Dict")
        # return

    return gene_Datadict


