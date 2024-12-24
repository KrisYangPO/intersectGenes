#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version1: 2024/12/16

from glob import glob
import os

# summarize input information into dictionary and subject it to pipeline:
def createInputDict(parse_out, DEG_selection):

    # setting input environment:
    path = parse_out.inputPath
    os.chdir(path)
    files = list(sorted(glob("*bed")))
    
    # determine mode: 
    # DEG:
    if parse_out.DEG:
        compareMode = "DEG"
        print("InputSummary: CompareMode is: ", compareMode)
        print("InputSummary: DEG selection condition: ", DEG_selection)
    
    # cluster
    elif parse_out.cluster:
        compareMode = "cluster"
        DEG_selection = False
        print("InputSummary: CompareMode is: ", compareMode)
        print("InputSummary: Mode-cluster: ", parse_out.cluster, "Mode-DEG: ", DEG_selection, parse_out.DEG)

    
    # create input dictionary:
    input_dict={
        "file_list":files,
        "index":parse_out.targetIndex,
        "mode": compareMode,
        "DESeq_file":parse_out.DEGFiles, 
        "DESeq_index": 0,
        "DEG_selection": DEG_selection,
        "outputname": parse_out.outputName,
        "outputpath": parse_out.outputPath,
        "cluster_indexes": parse_out.clusterIndexes}

    return input_dict

