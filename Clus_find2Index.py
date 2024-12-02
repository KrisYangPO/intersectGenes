#!/usr/bin/env python3
# cluster pipeline 
# Search compared index automatically based on a single index input.
# create: 2024/8/3 

"""
This script handles a merged data derived from two gene cluster files with same column-row format.
The comparison aims to find identical cluster group, and this script helps to find the column ID from a given index number.
Based on the file number, index, and whole length of merge dataframe, we can calculate the shift size that can iteratively find each target index.

However, the input files for this scripts are limit to a merged dataframe with identical column-row format, and the maximum merging data is 2. 
"""


# In[]
# Extract compared column indexes: 

# calculate the length of a single data column: 
# // divide (total column length) to (number of total input) == integer of the length of a single data columns.

def find2Index(merge_df, same_index, file_num):

    # calculate the columns length of a single dataframe:
    singleCol_num = len(merge_df.columns) // file_num 

    target_indexes = []
    target_cols = []
    shift = 0
    for i in range(0, file_num):
        
        # shift indicate the next compared index (assume that data are same col-row shape).
        shift += (singleCol_num * i)
        target_index = same_index + shift
        
        # if shifting is out of total column length, then stop shifting:
        if target_index < len(merge_df.columns): 
            target_indexes.append(target_index)
            target_cols.append(merge_df.columns[target_index])


    print("Target index: ", same_index)
    print("File number: ", file_num)
    print("single column number: ", singleCol_num)
    print("Target indexes: ", target_indexes)
    print("Target columns: ", target_cols)

    return target_indexes, target_cols
