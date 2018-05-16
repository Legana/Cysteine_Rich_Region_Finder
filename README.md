# Cysteine rich region finder (CCRF)

The CRRF analyses protein sequences in a FASTA format and counts the number of cysteines in a given amino acid window.
It is designed to capture cysteine rich regions in a protein sequence.

For usage and arguments use **-h**:

```bash
./CCRF.py -h
```

# CCRF usage examples

#use CCRF with default settings
```bash
./CCRF.py myfastafile.fasta
```

#change window size from default (30) to 60 amino acids
```bash
./CCRF.py -w 60 myfastafile.fasta
```

#change window size and change the cysteine rich index output from default (5) to 6 amino acids
```bash
./CCRF.py -w 60 -m 6 myfastafile.fasta
```

#change the frame size to advance by 10 amino acids at a time instead of default (1)
```bash
./CCRF.py -f 10 myfastafile.fasta
```

#change all default settings
```bash
./CCRF.py -m 6 -w 60 -f 10 myfastafile.fasta
```

# Installation and dependencies

Download CCRF.py

Note that CRRF requires Biopython (Cock et al. 2009) which can be obtained at [biopython.org](http://biopython.org/)

CRRF is written for Python 2.7

# Rational behind CRRF

Cysteine density of two toxin-focused databases: [Tox-Prot](https://www.uniprot.org/program/Toxins) and [ArachnoServer](https://www.uniprot.org/program/Toxins), and one general protein database: [SwissProt](http://www.uniprot.org/) was analysed with CRRF.
Cysteine density peaked around 6 cysteines in both ArachnoServer and Tox-Prot with a window size of 30, 50, and 100.
The highest peak occurred in a 30 amino acid window size. 5 cysteines were chosen as default for the CRRF to account for incomplete sequences.


![Cysteine density of three protein databases](https://github.com/Legana/Cysteine_Rich_Region_Finder/blob/master/db_cys_plot.png)

