'''
This script is to upload a bunch of contig files to PHASTER using their API. 
Author: Arif Mohammad Tanmoy
Email: arif.tanmoy@gmail.com
Use: python upload_contigs_to_PHASTER.py <contig folder>
*** All file in the <contig_folder> with ".fasta" extension will be considered as contig files. 

Citing PHASTER tool:
Arndt, D., Grant, J., Marcu, A., Sajed, T., Pon, A., Liang, Y., Wishart, D.S. (2016) PHASTER: a better, faster version of the PHAST phage search tool. Nucleic Acids Res., 2016 May 3.
'''

import sys, os
from os import listdir
from os.path import isfile, join

# Scan the folder for contig files (defined by ".fasta" suffix)
mypath = str(sys.argv[1])
contigs = [f for f in [join(mypath, a) for a in listdir(mypath) if isfile(join(mypath, a))] if f.endswith('.fasta')]

# UPLOAD the contigs to PHASTER
for i in range(0, len(contigs)):
	name = str(contigs[i]).split('/')[-1].split('.')[0]
	upload = 'cd '+mypath+' && '+'wget --post-file="'+str(contigs[i])+'" "http://phaster.ca/phaster_api?contigs=1" -O '+name+'.jobid'
	print "Uploading: "+name
	os.system(upload)

