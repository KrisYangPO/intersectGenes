#!/usr/bin/env python3
# hypergeometric: Clustering
# version1: 2024/12/6

import pandas as pd
import os
from glob import glob
from Clus_find2Index import *
from Clus_extractElements import *
from Clus_compareClus import *


# clustering Pipeline:
def cluster2Merged(input_dict, match_df):

    os.chdir(input_dict["outputpath"])
    outputname_clus = ("Cluster_" + input_dict["outputname"]).replace(".bed", ".xlsx")

    # In[]
    # Extract compared column indexes: 
    # Extrat compared column by target indexes:
    # Extract clusters from dataframe:
    compare_elements = extractElements(match_df, input_dict["cluster_indexes"])
    clusters, clusters_num = compare2Cluster(match_df, input_dict["cluster_indexes"], compare_elements)

    # In[]
    # Output the lengths of compared clusters:
    cluster_num_df = pd.DataFrame.from_dict(clusters_num, orient = "index")
    print(cluster_num_df)
    
    cluster_num_df.to_excel(outputname_clus.replace("Cluster_", "Cluster_SumN_"), index = "False", header = "Gene number")


    # Output compared clusters:
    with pd.ExcelWriter(outputname_clus) as w:

        for compare_id, df in clusters.items():
            df.to_excel(w, sheet_name = compare_id, index = False, header = match_df.columns)


    return clusters



# clustering Pipeline:
def clustersMerged_multi(input_dict, match_df):

    os.chdir(input_dict["outputpath"])
    outputname_clus = ("Cluster_" + input_dict["outputname"]).replace(".bed", ".xlsx")

    # In[]
    # Extract compared column indexes: 
    # Extrat compared column by target indexes:
    # Extract clusters from dataframe:
    compare_elements = extractElements(match_df, input_dict["cluster_indexes"])
    clusters, clusters_num = compareMulti_clusters(match_df, input_dict["cluster_indexes"], compare_elements)

    print("ClusterReport: Clustering is finished !!")
    
    # In[]
    # Output the lengths of compared clusters:
    cluster_num_df = pd.DataFrame.from_dict(clusters_num, orient = "index")
    print("ClusterReport: Clustering summary: \n", cluster_num_df)
    
    cluster_num_df.to_excel(outputname_clus.replace("Cluster_", "Cluster_SumN_"), index = "False", header = "Gene number")


    # Output compared clusters:
    with pd.ExcelWriter(outputname_clus) as w:

        for compare_id, df in clusters.items():
            df.to_excel(w, sheet_name = compare_id, index = False, header = match_df.columns)


    print("ClusterReport: Clustered files have been saved. Program completed !!")
    return clusters
