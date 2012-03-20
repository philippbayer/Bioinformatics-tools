#!/usr/bin/python

"""Takes a file in fasta-format and paints a histogram 
of that file's sequence-lengths using R.

Right now without any additional R-packages, too 
Remember to pipe into R using | R --vanilla

Arguments: Required is the file-name of the fasta-file.
Optional is --output <filename> to change the name of the PDF R creates.

Usage-scenario:
./SequenceLengthHistogram.py myfile.fasta --output blergs.pdf | R --vanilla
"""

import argparse
from Bio import SeqIO

def print_list_to_R(list):
    string = ""
    string += "x <- c(" 
    for element in list[:len(list)-1]:
        string += str(element) + ","
    string += str(list[len(list)-1]) + ")\n"
    string += "pdf('" + args.output + "')\n"
    string += "hist(x, ylab='count', xlab='Read-length', main='Distribution of Read-lengths')\ndev.off()\nquit()\n"
    print(string)


# build the parser, only one argument (file-directory)
parser = argparse.ArgumentParser(description='Takes a fasta-file, shows histogram of sequence-lengths')
parser.add_argument(dest='file', help='The fasta-file.')
parser.add_argument("--output", default="histogram.pdf", 
help="""Name of the output-PDF containing the histogram (default: histogram.pdf)""")

args = parser.parse_args()

# make a list containing all sequence-lengths from given file
lengths = [len(record) for record in SeqIO.parse(open(args.file), "fasta")]
print_list_to_R(lengths)
