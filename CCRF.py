#!/usr/bin/env python

# Calculating the cysteine density in a moving frame window for FASTA file containing numerous sequences

#to keep the program for general use, argparse and sys used to allow the input pile to be user defined through the command line

import argparse
import sys
import string

CYSTEINE = 'C'

parser = argparse.ArgumentParser(description='Calculate cysteine density for protein sequences.')

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),default=sys.stdin)

#defining options that are able to be set through the command line

parser.add_argument('-m','--min-count', type=int, default=5, help='Minimum number of cysteines within window to call a cysteine rich region (CRR)')
parser.add_argument('-w','--window', type=int, default=30, help='Size of window over which cysteine counts are calculated')
parser.add_argument('-f','--frame', type=int, default=1, help='Length of moving frame')

args = parser.parse_args()

#import FASTA file
from Bio import SeqIO
for record in SeqIO.parse(args.infile, "fasta"):
    seq = str(record.seq)

    CRRFound = False;
    max_c_count = 0

    #Looping through sequence, by size FRAME_ADVANCE
    for i in range(0, len(seq), args.frame):
        frame = seq[i:args.window+i]
        cCount = 0;

        cCount = string.count(frame,CYSTEINE)
        #Count how many cysteines are in each frame

        if ( cCount > max_c_count):
            max_c_count = cCount;

        #Does cysteine rich region exist?
        if (cCount >= args.min_count):
            CRRFound = True;

#print sequence ID, the maximum number of cysteines (CRR index) and presence of CRR
    print record.id + "\t" + str(max_c_count) + "\t" + str(CRRFound)
