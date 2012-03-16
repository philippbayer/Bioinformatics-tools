#!/usr/bin/python
"""Converts Genbank-files in a given directory to fasta-files 

while leaving the input-files intact.

Usage:

./GenbankToFasta.py -d {directory}

./GenbankToFasta.py -d /somewhere/on/my/system

"""

from Bio import SeqIO
import os, argparse

# build the parser, only one argument (file-directory)
parser = argparse.ArgumentParser(description='Converts all Genbank-files in the given directory to fasta-files. Leaves original files intact.')
parser.add_argument('-d', help='The directory in which the Genbank-files are located.')

args = parser.parse_args()

# go through all elements of the directory given,
# convert the ones ending in .gb
counter = 0
for element in os.listdir(vars(args)['d']):
    # if the lower-case version of an element ends in
    # .gb it's probably a Genbank-file
    if element.lower().endswith(".gb"):
        # open input/output-files
        file_handle = open(element)
        output_handle =  open(element.replace(".gb", ".fasta"), "w")
        # parse input and write to output
        for seq_record in SeqIO.parse(file_handle, "genbank"):
            output_handle.write(">%s %s\n%s\n" % (
                seq_record.id,
                seq_record.description,
                seq_record.seq))
        output_handle.close()
        file_handle.close()
        counter += 1

print "Done! Converted " + str(counter) + " files to fasta-format."
