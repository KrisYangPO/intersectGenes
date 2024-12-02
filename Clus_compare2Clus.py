#!/usr/bin/env python3
# cluster pipeline 
# Create Compared dataframe 
# create: 2024/8/3

"""
This script can only handle a pair of comparison by indicating two indexes and the compared elements
The first group of elements from the first compared columns will be select first iteratively, followed by the second group. 
"""

# Cluster into each comparison from a merged dataframe using two indicator indexes and compared elements. 
def compare2Cluster(merge_df, index_list, compare_elements):
    clusters = {}
    clusters_num = {}

    # Call each compared elements (clusters from 1st column and clusters from 2nd column)
    for i in range(0, len(compare_elements)):

        # Make sure the next index will not be out of length of compare_dict:
        if (i+1) < len(compare_elements):

            # Pick up the first compared cluster element:
            for clus1 in compare_elements[i]:
                merge_df2 = merge_df[merge_df.iloc[:,index_list[i]] == clus1]

                # Select the second compared cluster element:
                for clus2 in compare_elements[i+1]:
                    merge_df3 = merge_df2[merge_df2.iloc[:, index_list[i+1]] == clus2]

                    # Collect the comparison
                    clusters[(clus1 + "_vs_" + clus2)] = merge_df3
                    clusters_num[(clus1 + "_vs_" + clus2)] = len(merge_df3)

    
    return clusters, clusters_num
    
