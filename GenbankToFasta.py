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
parser.add_argument('dir', help='The directory in which the Genbank-files are located.')

args = parser.parse_args()

# go through all elements of the directory given

for element in os.listdir(vars(args)['dir']):
    if os.path.isfile(element):

        # open input/output-files
        file_handle = open(element)

        # parse through the file, collect all Genbank-items
        # (if they exist)
        seq_elements = []
        for seq in SeqIO.parse(file_handle, "genbank"):
            seq_elements.append(seq)

        file_handle.close()

        # is the file we parsed a Genbank-file?
        if len(seq_elements) != 0:
            # (re)name the file to fasta
            if "." in element:
                filename = element[:element.find(".")] + ".fasta"
            else:
                filename = element + ".fasta"

            # open output
            output_handle =  open(filename, "w")
            # iterate over all genbank-items
            for seq in seq_elements:
                output_handle.write(">%s %s\n%s\n" % (
                    seq.id,
                    seq.description,
                    seq.seq))
            output_handle.close()

