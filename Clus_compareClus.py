#!/usr/bin/env python3
# cluster pipeline 
# Create Compared dataframe 
# create: 2024/12/6

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

        # Make sure the next index do not exceed length of compare_dict:
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




# Multi-Clustering 
def compareMulti_clusters(merge_df, index_list, compare_elements):
    
    # check input information:
    if len(index_list) != len(compare_elements):
        print("ClusterERROR: The number of target indexes: ", len(index_list), " is not match with that of the target elements: ", len(compare_elements), ". \n !! Abort !!")
        return
    
    else: 
        for index, element in zip(index_list, compare_elements): 
            targets = sorted(list(set(merge_df.iloc[:,index])))

            for e in element: 
                # check if target elements is present in dataframe. 
                if e not in targets:
                    print("ClusterERROR: The target element: ", e, " is absent in dataframe: ", targets, ". Abort !!")
                    return
                else:
                    print("ClusterReport: Start to separate each cluster: ", e)



    # Start to separate and store each comparison: 
    clusters = {}
    clusters_num = {}

    # call each list of the elements from target column:
    for i in range(0, len(compare_elements)):

        # call the next elements from the next target column: 
        # i+1 iteratively denote the next target index:
        # len(compare_elements) is the end of the calling elements:
        for i2 in range(i + 1, len(compare_elements)):

            # indicate each list of the elements from the target column:
            # i for the first, and i2 for the second target:
            clus1_list = compare_elements[i]
            clus2_list = compare_elements[i2]
            index1 = index_list[i]
            index2 = index_list[i2]

            # call each element from target list: 
            for clus1 in clus1_list:
                for clus2 in clus2_list: 
                    print("ClusterReport: Comparison: ", index1, ":" , clus1, " vs ", index2, ":", clus2)

                    # selection    
                    selection = (merge_df.iloc[:, index1] == clus1) & (merge_df.iloc[:, index2] == clus2)
                    merge_df2 = merge_df[selection]
                    comparison = "{0} v.s. {1}".format(clus1, clus2)

                    # store in clusters dictionary
                    clusters[comparison] = merge_df2
                    clusters_num[comparison] = len(merge_df2)


    return clusters, clusters_num





# main test     
def main():
    import pandas as pd

    # path
    p = r"/Users/popoyang/Documents/Coding/Python/NGS/hypergeometric(HypGeo)/HypGeo_*newAlgo/test/Test_clustering/"
    out = p + "output/"
    file = r"MERGE_DEGs_heatmap_refGene_log2_TERC_vs_SC_CCAR1.bed"
    outname = r"Cluster_" + file.replace("bed", "xlsx")

    # input
    df = pd.read_csv(p + file, sep = "\t")
    index_list = [8, 14, 21]
    compare_elements = [['DOWN', 'UP'], ["+", "-"], ['cluster_1', 'cluster_2', 'cluster_3']]


    # clustering:
    clusters, clusters_num = compareMulti_clusters(df, index_list, compare_elements)


    # output 
    cluster_num_df = pd.DataFrame.from_dict(clusters_num, orient = "index")
    cluster_num_df.to_excel(out + "NumSum" + outname, index = "False", header = "Gene number")
    print(cluster_num_df)

    
    # output compared clusters:
    with pd.ExcelWriter(out + outname) as w:
        for compare_id, df in clusters.items():
            df.to_excel(w, sheet_name = compare_id, index = False, header = df.columns)


# call function
if __name__ == "__main__":
    main()
