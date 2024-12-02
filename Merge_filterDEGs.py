#!/usr/bin/env python3
# multiple selection of DEGs 
# create: 2024/7/9

"""
For selecting DEGs, the program considers 3 factors: p-value, p.adj, and foldchange.
Create Factor:threshold dictionary, and use dataframe indexing to select threshold. 
For foldchange selection, the selection have to be either higher than positive threshold or lower than negative threshold.
"""

# In[] function call

def multiselect_DEG(df, select, value):
    # check whether number of select and its values is equivalent.
    if len(select) != len(value):
        print("FilterDEGs: Missing value or missing target")
        return
    
    # create selection target and its threshold value:
    threshold = dict(zip(select, value))

    # iteratively filter out expected data via targeted column: 
    for i in range(0, len(select)):
        select_col = select[i]

        # check whether target column presents in columns of DESeq table.
        if select_col in list(df.columns):
            
            # sift log2foldchange selection with both up and down regulation:
            if select_col == "log2FoldChange":
                df = df[(df[select_col] > threshold[select_col]) | (df[select_col] < -(threshold[select_col]))]  
            # filter pvalue or padj value:
            else: df = df[df[select_col] < threshold[select_col]]
        
        else:
            print("FilterDEGs: Unknown column ID: ", select_col)
            return

    # return selected dataframe
    return df.dropna()

