#!/usr/bin/env python3
# multiple selection of DEGs 
# create: 2024/7/9

"""
For selecting DEGs, the program considers 3 factors: p-value, p.adj, and foldchange.
Create Factor:threshold dictionary, and use dataframe indexing to select threshold. 
For foldchange selection, the selection have to be either higher than positive threshold or lower than negative threshold.
"""

# In[] function call
def multiselect_DEG(df, select, value):
    # check whether number of select and its values is equivalent.
    if len(select) != len(value):
        print("FilterDEGs: Missing value or missing target")
        return
    
    # create selection target and its threshold value:
    threshold = dict(zip(select, value))

    # iteratively filter out expected data via targeted column: 
    for i in range(0, len(select)):
        select_col = select[i]

        # check whether target column presents in columns of DESeq table.
        if select_col in list(df.columns):
            
            # sift log2foldchange selection with both up and down regulation:
            if select_col == "log2FoldChange":
                df = df[(df[select_col] > threshold[select_col]) | (df[select_col] < -(threshold[select_col]))]  
            # filter pvalue or padj value:
            else: df = df[df[select_col] < threshold[select_col]]
        
        else:
            print("FilterDEGs: Unknown column ID: ", select_col)
            return

    # indicates DEGs based on Log2Foldchange values:
    df["DEGs_indicator"] = "DOWN"
    df.loc[df["log2FoldChange"] > 0, "DEGs_indicator"] = "UP"


    # return selected dataframe
    return df.dropna()



# Advanced DEGs selection:
def multiselect_DEG_advanced(df, select, value, mode):
    # check whether number of select and its values is equivalent.
    if len(select) != len(value):
        print("FilterDEGs: Missing value or missing target")
        return   
    

    # check whether selectors are present in DESeq2 table columns:
    for sel in select: 
        if sel not in df.columns:
            print("ERROR(FilterDEGs): Unknown column ID: ", sel, "...Abort.")
            return


    # iteratively filter out expected data via targeted column:
    # report selection conditions:
    report = {"Select column":[],
              "Select mode": [],
              "threshold": [],
              "selected size": [], 
              "Stat": []} 

    for i in range(0, len(select)):
        select_target = select[i]
        select_mode = mode[i]
        select_value = value[i]
        size = len(df)
        stat = "OK"


        # select above value or below value:
        if (select_mode).upper() == "BELOW":
            selection = df[select_target] < select_value
            df = df[selection]
            size = len(df)

        elif (select_mode).upper() == "ABOVE":
            selection = df[select_target] > select_value
            df = df[selection]
            size = len(df)

        # select values in a range or outer a range: 
        elif (select_mode).upper() in ["RANGE", "OUTER"]:
            
            # check whether there are two value in the mode:
            # check whether min value < max value:
            if (len(select_value) > 1) and (select_value[0] < select_value[1]):
                selection = ( df[select_target] > select_value[0]) & (df[select_target] < select_value[1])
                
                if (select_mode).upper() == "RANGE":
                    df = df[selection]
                    size = len(df)

                elif (select_mode).upper() == "OUTER":
                    df = df[~selection]
                    size = len(df)

            else: 
                if len(select_value) <= 1:
                    print("ERROR(FilterDEGs): Choose mode: ", select_mode, " with its value: ", select_value, "\n\t", "Missing values for range.")
                    return
                elif select_value[0] >= select_value[1]:
                    print("ERROR(FilterDEGs): minimum value: ", select_value[0], " should lower than Maximum value: ", select_value[1])
                    return 
            

        # report unknown selector:     
        else:
            print("ERROR(FilterDEGs): Selection mode: ", select_mode, " was not defined for any selection way. Abort.")
            print("ERROR(FilterDEGs): Available selections include: Below, Above, Range, and Outer.")
            return
        
        
        # report selection state     
        if size < 1:
            stat = "Selection TOO Strong"
            print("WARNING(FilterDEGs): No Remaining data after selection: ", select_target, " with value: ", select_value)


        # Report storing:
        report["Select column"].append(select_target)
        report["Select mode"].append(select_mode)
        report["threshold"].append(select_value)
        report["selected size"].append(size)
        report["Stat"].append(stat)


    # indicates DEGs based on Log2Foldchange values:
    df["DEGs_indicator"] = "DOWN"
    df.loc[df["log2FoldChange"] > 0, "DEGs_indicator"] = "UP"
    
    # return selected dataframe
    return df.dropna(), report




# In[] test
def main():
    import pandas as pd
    p = r"/Users/popoyang/Documents/Coding/Python/NGS/hypergeometric(HypGeo)/HypGeo_*newAlgo/test/"
    df = pd.read_csv(p + "DESeq2_geneDEG.txt", sep = "\t")
    #print(df)

    select = ["pvalue", "padj", "log2FoldChange"]
    value = [0.05, 0.05, [-1,1]]
    mode = ["BELOW", "BELOW", "RANGE"]

    # select = ["log2FoldChange"]
    # value = [[-1,1]]
    # mode = ["RANGE"]

    df2, report_dict = multiselect_DEG_advanced(df, select, value, mode)
    df2_report = pd.DataFrame(report_dict)

    print(df2.head(5))
    print(df2_report)

# call function
if __name__ == "__main__":
    main()
