# testing EXXE_parseinput.py 


# Example: DEG mode
input_p=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_reverse/
output_file=MERGE_DEGs_padj0.05_CCAR1.bed
input_index=3
deg=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_DEG_select/DESeq2_geneDEG.txt

/Users/popoyang/Documents/Coding/Git_repos/hyperIntersect/EXE_MergeCluster_parse_v5.py \
 --inputPath ${input_p} \
 --outputName ${output_file} \
 --outputPath ${input_p}output/ \
 --targetIndex ${input_index} \
 --DEG \
 --DEGFiles ${deg} \
 --pvalue 0.05 \
 --padj 0.05 \
 --log2FC -1 1 \
 --selectionMmode range \
 --clusterIndexes 7 20


# # cluster mode
# input_p=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_clusterMode/
# output_file=MERGE_CCAR1_vs_PolIIS5.bed
# input_index=3
# # deg=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_DEG_select/DESeq2_geneDEG.txt

# /Users/popoyang/Documents/Coding/Git_repos/hyperIntersect/EXE_MergeCluster_parse_v5.py \
#  --inputPath ${input_p} \
#  --outputName ${output_file} \
#  --outputPath ${input_p}output/ \
#  --targetIndex ${input_index} \
#  --cluster \
#  --clusterIndexes 12 25

 
# # reverse test:
# input_p=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_reverse/
# output_file=MERGE_DEGs_padj0.05_CCAR1.bed
# input_index=3
# deg=/Users/popoyang/Documents/Coding/Python/NGS/mergeIntersect/mergeIntersect_parse/test/Test_DEG_select/DESeq2_geneDEG.txt

# /Users/popoyang/Documents/Coding/Git_repos/hyperIntersect/EXE_MergeCluster_parse_v5.py \
#  --inputPath ${input_p} \
#  --outputName ${output_file} \
#  --outputPath ${input_p}output/ \
#  --targetIndex ${input_index} \
#  --DEG \
#  --DEGFiles ${deg} \
#  --pvalue 0.05 \
#  --padj 0.05 \
#  --log2FC -1 1 \
#  --reverse \
#  --selectionMmode range \
#  --clusterIndexes 7 20 


