#!/usr/bin/env python3
# hypergeometric: find overlapped genes
# using isin() function
# version1: 2023/04/18

"""
This script only merges two dataframe into one based on their co-exist genes.
However, the clusters of each dataframe is still not separated in this job. 
"""

import os
from glob import glob
from PIPE_merge import *


# # In[] DEG mode
# # find overlapping genes from DEGs and merged-replicated clusters. 

# path = r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_DEGs_vs_PolIIS5/"
# os.chdir(path)

# input={
#     "file_list":list(sorted(glob("*bed"))),
#     "index":3,
#     "mode": r"DEG",
#     "DESeq_file": r"/Users/popoyang/Documents/R807/Publication/TERC_Epigenetic/Analyses/RNA_seq/TERC_KD/DESeq_output/DESeq2_geneDEG.txt",
#     "DESeq_index": 0,
#     "select":["pvalue","padj"],
#     "value":[0.05, 0.05],
#     "outputname": r"MERGE_DEGs_padj0.05_PolIIS5.bed",
#     "outputpath": path
# }

# # find overlapping genes from DEGs and merged-replicated clusters.
# match, unmatch = compare_DEGsMerge(input)



# # In[] cluster mode 
# # find overlapping genes betweeen two replicated clusters

# path = r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_PolIIS5_vs_Wdr82"
# os.chdir(path)

# input={
#     "file_list":list(sorted(glob("*bed"))),
#     "index":3,
#     "mode": r"clusters",
#     "outputname": r"MERGE_PolIISer5_vs_Wdr82.bed",
#     "outputpath": r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_PolIIS5_vs_Wdr82/"
# }

# # find overlapping genes from DEGs and merged-replicated clusters.
# match, unmatch = compare_mergeMulti(input)



# In[] test multiple files with DEG mode
# find overlapping genes from DEGs and merged-replicated clusters. 

path = r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_DEGs_vs_Wdr82/"
os.chdir(path)

input={
    "file_list":list(sorted(glob("*bed"))),
    "index":3,
    "mode": r"DEG",
    "DESeq_file": r"/Users/popoyang/Documents/R807/Publication/TERC_Epigenetic/Analyses/RNA_seq/TERC_KD/DESeq_output/DESeq2_geneDEG.txt",
    "DESeq_index": 0,
    "select":["pvalue","padj"],
    "value":[0.05, 0.05],
    "outputname": r"MERGE_DEGs_padj0.05_Wdr82.bed",
    "outputpath": path
}

# find overlapping genes from DEGs and merged-replicated clusters.
match, unmatch = compare_DEGsMerge(input)
