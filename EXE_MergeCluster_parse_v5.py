#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version 3: 2024/12/12

import pandas as pd
from glob import glob
from PIPE_Parse import *
from PIPE_merge import *
from PIPE_cluster import * 


# invoke:
def main():  
    input_dict = summarizeInput()

    if input_dict:

        # find out overlapping genes from DEGs and merged-replicated clusters.
        # perform DEGs compare:
        if input_dict["mode"] == "DEG":
            match, unmatch = compare_DEGsMerge(input_dict)
        
        # perform total compare:
        elif input_dict["mode"] == "cluster": 
            match, unmatch = compare_mergeMulti(input_dict)


        else: print("InputSummary: Unknown Mode: ", input_dict["mode"])
        
        # clustering:
        cluster_dicts = clustersMerged_multi(input_dict, match)

    else:
        print("InputSummaryError: Check summarizeInput().")
        return


# call function
if __name__ == "__main__":
    main()
