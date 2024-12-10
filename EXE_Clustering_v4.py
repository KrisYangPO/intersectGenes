#!/usr/bin/env python3
# handle clustering 
# create: 2024/12/6

import os
from glob import glob
from PIPE_merge import *
from PIPE_cluster import *


# DEG clustering:
path = r"/Users/popoyang/Documents/R807/NGS/20th_TERCkd_CutRun_MERGE/hypergeometric/Merge_DEGs_vs_CCAR1/"
os.chdir(path)

input={
    "file_list":list(sorted(glob("*bed"))),
    "index":3,
    "mode": r"DEG",
    "DESeq_file": r"/Users/popoyang/Documents/R807/Publication/TERC_Epigenetic/Analyses/RNA_seq/TERC_KD/DESeq_output/DESeq2_geneDEG.txt",
    "DESeq_index": 0,
    "select":["pvalue", "padj"],
    "value":[0.05, 0.05],
    "Select_mode": ["BELOW", "BELOW"],
    "outputname": r"MERGE_DEGs_padj0.05_CCAR1.bed",
    "outputpath": path + "output/", 
    "cluster_indexes": [7, 20]
}

# find overlapping genes from DEGs and merged-replicated clusters.
match, unmatch = compare_DEGsMerge(input)
cluster_dicts = clustersMerged_multi(input, match)

# print(cluster_dicts)


