#!/usr/bin/env python3
# cluster pipeline 
# extract compared elements 
# create: 2024/8/3 

# Extrat compared column by target indexes:
def extractElements(merge_df, index_list): 
    
    compare_elements = []
    for i in index_list:

        print("Target column: ", merge_df.columns[i])
                
        # find elements from the target column, and remove duplicates by set() function:
        compare_elements.append(sorted(list(set(merge_df.iloc[:,i]))))

    print("Target elements: ", compare_elements)
    return compare_elements
