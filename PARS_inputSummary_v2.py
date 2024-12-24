#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version1: 2024/12/16

from glob import glob
import os

# summarize input information into dictionary and subject it to pipeline:
def createInputDict(parse_out, DEG_selection):

    # setting input environment:
    # if the input files were specified:
    if parse_out.inputfiles is not False:
        path = parse_out.inputPath
        files = parse_out.inputfiles
        files = [path + file for file in files]
    
    # if the input files were not specified:
    # use glob to gather all files from the inputpath:
    # parameter: inputformat must be added. 
    else:  
        path = parse_out.inputPath
        os.chdir(path)
        files_list = list(sorted(glob("*")))

        # filter out non-target cluster or data files
        files = []
        for file in files_list:

            # check whether file format is specified:
            if parse_out.inputformat:
                # check file contains format string:
                if parse_out.inputformat in file: 
                    files.append(file)
                else:
                    print("InputSummaryERROR: File format Error with file: {0} and input format: {1}, Abort this: {2}.".format(file, parse_out.inputformat, file))
            else:
                print("InputSummaryERROR: File format must be given, if --inputfiles was not defined.")

        # make sure there is at least one file is imported. 
        if files:
            print("InputSummary: Received input files.")
        else:
            print("InputSummaryERROR: There is empty input files!! Abort.")
            return
    
    

    # determine mode: 
    # DEG:
    if parse_out.DEG:
        compareMode = "DEG"
        DEG_selection = DEG_selection
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
