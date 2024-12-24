#!/usr/bin/env python3
# hypergeometric: setting parsing input
# version1: 2024/12/16

import argparse

def parseInput():
    prog_parse = argparse.ArgumentParser(
        prog = "mergeClusters",
        description = "Perform EXE_merge / EXE_cluster", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
        epilog = "If you encounter any problem, please feel free to reach out PO.")

    prog_parse.add_argument(
        "-p", "--inputPath", 
        type = str,
        help = "indicate your working directory of the input files.",
        default = "./",
        required = True)
    
    prog_parse.add_argument(
        "-inf", "--inputfiles", 
        type = str,
        nargs = "+",
        help = "indicate the input files.",
        default = False,
        required = False)
    
    prog_parse.add_argument(
        "--inputformat", 
        type = str,
        help = "indicate the format of the input files.",
        default = "bed",
        required = False)

    prog_parse.add_argument(
        "--outputName", 
        type = str,
        help = "indicate the prefix of the output files.",
        default = "MERGED_file.bed", 
        required = True)

    prog_parse.add_argument(
        "-o", "--outputPath", 
        type = str,
        help = "indicate the directory for output files.",
        default = "./", 
        required = True)

    prog_parse.add_argument(
        "-i", "--targetIndex", 
        type = int,
        nargs = 1,
        required = True, 
        help = "Specify the column index number for finding overlapping information \
            (ex: Gene ID column index).")



    # selection mode: conflict input: 
    Compare_mode = prog_parse.add_mutually_exclusive_group()
    Compare_mode.add_argument(
        "--DEG", 
        action="store_true", 
        help = "Compare the items of the target column to DEGs to find intersected data. ")
    
    Compare_mode.add_argument(
        "--cluster", 
        action="store_true", 
        help = "Compare the items of the target column to DEGs to find intersected data. ")



    # DEG-specific parameters:
    prog_parse.add_argument(
        "--DEGFiles", 
        type = str,
        help = "Specify the raw information of the DEGs (ex: DESeq2 output table).")

    prog_parse.add_argument(
        "--pvalue", 
        type = float,
        nargs = 1,
        default = False,
        help = "DEGs with pvalue default cutoff: 0.05.")

    prog_parse.add_argument(
        "--padj", 
        type = float,
        nargs = 1,
        default = False, 
        help = "DEGs with padj default cutoff: 0.05.")

    prog_parse.add_argument(
        "--log2FC", 
        type = float,
        nargs = 2,
        default = False, 
        help = "DEGs with log2foldchange cutoff. \
            The first num is lower limit and the second is upper limit.")

    prog_parse.add_argument(
        "--selectionMmode", 
        type = str,
        default = False, 
        help = "For --log2FC or other range selection, \
            selection-mode determine whether to select DEGs within or outside of its. \
            \nAvailable options: range, outer.")

    prog_parse.add_argument(
        "--reverse", 
        action="store_true", 
        default = False, 
        help = "Determin whether to use below or above the cutoff value for DEGs selection. \
            Default: Below.\n reverse will turn Beloww into Above.")


    # cluster:
    prog_parse.add_argument(
        "--clusterIndexes", 
        type = int,
        nargs = "+",
        help = "Specify the target column indexes for splitting the clusters based on your selected columns. ")

    # invoke parsing:
    inputProg = prog_parse.parse_args()

    # report 
    blank = 20
    print(f"{"Input path:":<{blank}} {inputProg.inputPath}")
    print(f"{"Input file:":<{blank}} {inputProg.inputfiles}")
    print(f"{"Input format:":<{blank}} {inputProg.inputformat}")
    print(f"{"Output name:":<{blank}} {inputProg.outputName}")
    print(f"{"Output path:":<{blank}} {inputProg.outputPath}")
    print(f"{"Target column:":<{blank}} {inputProg.targetIndex}")
    print(f"{"Mode-DEG:":<{blank}} {inputProg.DEG}")
    print(f"{"Mode-cluster:":<{blank}} {inputProg.cluster}")
    print(f"{"DEG file:":<{blank}} {inputProg.DEGFiles}")
    print(f"{"pvalue:":<{blank}} {inputProg.pvalue}")
    print(f"{"padj:":<{blank}} {inputProg.padj}")
    print(f"{"Log2FC:":<{blank}} {inputProg.log2FC}")
    print(f"{"Select mode:":<{blank}} {inputProg.selectionMmode}")
    print(f"{"Reverse select:":<{blank}} {inputProg.reverse}")
    print(f"{"Cluster indexes:":<{blank}} {inputProg.clusterIndexes}")


    return inputProg

