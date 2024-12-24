#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version 3: 2024/12/12

import pandas as pd
from PARS_inputArgpars import *
from PARS_checkInput_v2 import *
from PARS_inputDict_v2 import *

# invoke:
def summarizeInput():  

    # input summary: 
    inputProg = parseInput()
    input_summary = checkInputMode(inputProg)

    check = input_summary[0]
    parseOut = input_summary[1]
    DEG_condition = input_summary[2]
    

    # check summary check is True:
    if check:
        print("InputDict: CheckInput: {}".format(check))

        if inputProg.DEG:
            DEG_condition_df = pd.DataFrame(DEG_condition, index = ["Select", "Cutoff"]).T 
            print("InputDict: Mode is DEG.")
            print("InputDict: DEG condition: \n", DEG_condition_df)

        elif inputProg.cluster: print("InputDict: Mode is cluster.")


        # gain input information from parse. 
        input_dict = createInputDict(parse_out = parseOut , DEG_selection = DEG_condition)

        # show all parameters again:
        for i, j in input_dict.items(): print(f"{i:<{30}} {j}")

        # return to pipeline
        return input_dict
    
    
    else:
        print("CheckInputERROR: Erroneous input information. Abort.")
        return




