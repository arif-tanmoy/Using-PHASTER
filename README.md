# Working_with_PHASTER
A few scripts to upload multiple contig files to PHASTER (*using API*), check if the results are ready and download the summary results in a file. I hope, these will help to make someone's life a bit more easier. 

## What is PHASTER?
PHASTER (PHAge Search Tool Enhanced Release) is a web server for the rapid identification and annotation of prophage sequences within bacterial genomes and plasmids. 

### Intro and use for each of the scripts
#### upload_contigs_to_PHASTER.py
The script will scan the the folder for *.fasta* files and upload those files to PHASTER using public API. PHASTER server relays back a JOBID. This script will receive the JOBID from PHASTER and save it in a *.jobid* file in the same folder. USE:
```
python upload_contigs_to_PHASTER.py <contig folder>
```


```
*More scripts are coming*
```

### Citing PHASTER article:
[Arndt D, Grant JR, Marcu A, Sajed T, Pon A, Liang Y, Wishart DS. PHASTER: a better, faster version of the PHAST phage search tool. Nucleic Acids Res. 2016 Jul 8;44(W1):W16-21. doi: 10.1093/nar/gkw387. Epub 2016 May 3. PMID: 27141966; PMCID: PMC4987931.](https://pubmed.ncbi.nlm.nih.gov/27141966/).
