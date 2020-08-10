# sarscov2barcode

![alt text](https://github.com/raeece/sarscov2barcode/blob/master/genotype.jpg?raw=true)

## Prerequisites

- python3
  - scikit-allel
  - pandas
  - numpy
- bcftools (http://www.htslib.org/download/)

## Instructions

1. Map the reads using bwa or bowtie to obtain bam files
2. Run the bcftools command and pipe the vcf output to assignclade.py script

```
bcftools mpileup \
-f GCF_009858895.2_ASM985889v3_genomic.fna sample_1_sorted.bam \
| bcftools call --ploidy 1 -mv -Ov \
| python3 assignclade.py
```

## Output

```bcftools mpileup -f GCF_009858895.2_ASM985889v3_genomic.fna sample_1_sorted.bam | bcftools call --ploidy 1 -mv -Ov | python3 assignclade.py

{241: 'T', 3037: 'T', 14408: 'T', 23403: 'G', 27904: 'C', 28854: 'T'}

Sample ['C' 'T' 'G' 'T' 'T' 'T' 'G' 'G' 'T' 'G' 'G']
Match  ['|' '|' '|' '|' '|' '|' '|' '|' '|' '|' '|']
Clade G['C' 'T' 'G' 'T' 'T' 'T' 'G' 'G' 'T' 'G' 'G']
Clade G matches 100%
```

## Citation

Qingtian Guan, Mukhtar Sadykov, Raushan Nugmanova, Michael J. Carr, Stefan T. Arold,Arnab Pain.<br/>
The genomic variation landscape of globally-circulating clades of SARS-CoV-2 defines a genetic barcoding scheme
doi: https://doi.org/10.1101/2020.04.21.054221
