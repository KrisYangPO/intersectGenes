#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version1: 2024/12/16

"""
parse_out.reverse determine whether cutoff values of the DEGs should be
below or above the threshold. Default setting is "BELOW", however, adding 
 --reverse parameter revert the determination. 
"""


def checkInputMode(parse_out):

    # check Mode: 
    if parse_out.DEG:

        # determine whether DEGs should below or above pvalue = 0.05
        determine = ["BELOW"]
        if parse_out.reverse:
            determine = ["ABOVE"]
        

        # Create threshold dictionary (whether there is a value for each item):
        selection = ["pvalue", "padj", "log2FoldChange"]
        threshold = [parse_out.pvalue, parse_out.padj, parse_out.log2FC]
        DEG_select_Dict = dict(zip(selection, threshold))

        
        # Check whether there is no any selection items:
        test = list(DEG_select_Dict.values())
        test = [thres for thres in test if thres is not False]

        if test: check = True   
        else: 
            print("CheckInputERROR: Mode-DEG needs one or more DEG selection target (ex: pvalue, padj, or Log2FC).")
            check = False 
            return [check, parse_out, DEG_select_Dict]


        # Remove selection with non-assigned threshold value:
        # Create another DEG_select_Dict2 to store true selection with correct threshold value:
        DEG_select_Dict2 = {}
        for key, value in DEG_select_Dict.items():
            # add true selection with correct threshold value:            
            if value is not False: 
                DEG_select_Dict2[key] = value

            else:
                print("CheckInputReport: Selection: {} was not assigned any value, discard it.".format(key))



        # assign RANGE, BELOW, or ABOVE determinator to select DEGs:
        for key, value in DEG_select_Dict2.items():
            
            # pvalue and padj are supposed to have 1 cutoff value
            if len(value) == 1:
                DEG_select_Dict2[key] = determine + DEG_select_Dict2[key]

            # log2FC is supposed to have 2 cutoff values for ranging. 
            elif len(value) == 2:
                DEG_select_Dict2[key] = [parse_out.selectionMmode, DEG_select_Dict2[key]]

            else:
                print("CheckInputERROR: Erroneous condition of: {0} with its value: {1}".format(key, value))
                check = False
                return parse_out, DEG_select_Dict2, check
     
        
        return [check, parse_out, DEG_select_Dict2]
        


    # cluster files:
    elif parse_out.cluster:
        print("Checkpoint: Mode-Cluster activated.")
        check = True
        DEG_select_Dict = False

        return [check, parse_out, DEG_select_Dict]


