# testing EXXE_parseinput.py 

input_p=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_parsInput/
input_file=MERGE_DEGs_padj0.05_CCAR1.bed
input_index=3
deg=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_DEG_select/DESeq2_geneDEG.txt

/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/EXE_MergeCluster_parse_v5.py \
 --inputPath ${input_p} \
 --outputName ${input_file} \
 --outputPath ${input_p}output/ \
 --targetIndex ${input_index} \
 --DEG \
 --DEGFiles ${deg} \
 --pvalue 0.05 \
 --padj 0.05 \
 --log2FC -1 1 \
 --selectionMmode range \
 --clusterIndexes 7 20 
