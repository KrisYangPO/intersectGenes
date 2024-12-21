#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version1: 2024/12/21

"""
parse_out.reverse determine whether cutoff values of the DEGs should be
below or above the threshold. Default setting is "BELOW", however, adding 
 --reverse parameter revert the determination. 
"""


def checkInputMode(parse_out):
	
    # determine whether DEGs should below or above pvalue = 0.05
    determine = ["BELOW"]
    if parse_out.reverse:
        determine = ["ABOVE"]
	

    # check Mode: 
    if parse_out.DEG:
        
        # check whether there is one or more DEG selection item:
        if ((parse_out.pvalue) + (parse_out.padj) + (parse_out.log2FC)) != 0:
            check = True

            # create DEG selection dictionary:
            items = ["pvalue", "padj", "log2FoldChange"]
            value = [parse_out.pvalue, parse_out.padj, parse_out.log2FC]
            DEG_select_Dict = dict(zip(items, value))

            # remove False selection 
            # add indicator to tell whether DEGs should be above or below the cutoff, or within or outside a range.
            for item, value in DEG_select_Dict.items():
                if value == False:
                    print("Checkpoint: Selection: ", item, " was not assigned any value, discard it.")
                    del DEG_select_Dict[item]

                else:
                    # pvalue and padj are supposed to have 1 cutoff value
                    if len(value) == 1:
                        #DEG_select_Dict[item].append("BELOW")
                        DEG_select_Dict[item] = determine + DEG_select_Dict[item]

                    # log2FC is supposed to have 2 cutoff values for ranging. 
                    elif len(value) == 2:
                        #DEG_select_Dict[item].append(parse_out.selectionMmode)
                        DEG_select_Dict[item] = [parse_out.selectionMmode, DEG_select_Dict[item]]

                    else:
                        print("Checkpoint-Mode-DEGs: Can't detect the cutoff condition of: ", item, " value: ", value)
                        check == False
                        return parse_out, DEG_select_Dict, check

        # There is no selection items (pvalue, padj, or log2FC parameters) were assigned.
        else:
            print("Checkpoint-Mode-DEGs: Mode-DEG needs one or more DEG selection target (ex: pvalue, padj, or Log2FC)")
            check = False       
        
        return [check, parse_out, DEG_select_Dict]
        


    # cluster files:
    elif parse_out.cluster:
        print("Checkpoint: Mode-Cluster activated.")
        check = True
        DEG_select_Dict = False

        return [check, parse_out, DEG_select_Dict]



