
#!/usr/bin/env python3

input_file = "1_aln.txt"
output_file = "1_aln.sam"

# 给出 SAM header，你需要在这里指定参考序列长度（比如 188,307 bp）
reference_name = "NG_007726.3"
reference_length = 188307 # 请替换为真实长度，参考你的 reference.fa.fai

with open(input_file) as fin, open(output_file, "w") as fout:
    # 写 SAM header
    fout.write("@HD\tVN:1.0\tSO:unsorted\n")
    fout.write(f"@SQ\tSN:{reference_name}\tLN:{reference_length}\n")
    
    for line in fin:
        cols = line.strip().split("\t")
        qseqid, sseqid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = cols
        
        flag = 0 # 0 表示正向比对；如果 sstart > send 则表示反向
        if int(sstart) > int(send):
            flag = 16 # 反向链
            pos = int(send)
        else:
            pos = int(sstart)
        
        mapq = 255
        cigar = f"{length}M" # 简化处理，所有碱基都匹配
        rnext = "*"
        pnext = 0
        tlen = 0
        seq = "*"
        qual = "*"
        
        fout.write(f"{qseqid}\t{flag}\t{sseqid}\t{pos}\t{mapq}\t{cigar}\t{rnext}\t{pnext}\t{tlen}\t{seq}\t{qual}\n")


