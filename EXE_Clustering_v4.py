# handle clustering 
# create: 2024/7/29

import pandas as pd
import os
from glob import glob
from Clus_find2Index import *
from Clus_extractElements import *
from Clus_compare2Clus import *
from Merge_PIPE import *


# In[] test file
path = r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_PolIIS5_vs_Wdr82/"
os.chdir(path)

input={
    "file_list":list(sorted(glob("*bed"))),
    "index":3,
    "mode": r"clusters",
    "outputname": r"MERGE_PolIISer5_vs_Wdr82.bed",
    "outputpath": r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_PolIIS5_vs_Wdr82/output/",
    "cluster_indexes": [12, 25]
}


# find overlapping genes from DEGs and merged-replicated clusters.
match, unmatch = compare_mergeMulti(input)
os.chdir(input["outputpath"])
outputname_clus = ("Cluster_" + input["outputname"]).replace(".bed", ".xlsx")


# In[]
# Extract compared column indexes: 
# Extrat compared column by target indexes:
# Extract clusters from dataframe:
compare_elements = extractElements(match, input["cluster_indexes"])
clusters, clusters_num = compare2Cluster(match, input["cluster_indexes"], compare_elements)


# In[]
# Output the lengths of compared clusters:
cluster_num_df = pd.DataFrame.from_dict(clusters_num, orient = "index")
print(cluster_num_df)
cluster_num_df.to_excel("Nunmber_" + outputname_clus, index = "False", header = "Gene number")


# Output compared clusters:
with pd.ExcelWriter(outputname_clus) as w:

    for compare, df in clusters.items():
        sheetname = compare
        df.to_excel(w, sheet_name = sheetname, index = False, header = match.columns)


