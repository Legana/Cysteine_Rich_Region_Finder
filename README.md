# Cysteine rich region finder (CCRF)

Default settings are to count the maximum number of cysteines in a window size of 30 advancing by 1 frame (amino acid) at a time

To change the window size use the option -w ##
To change the frame size use the option -f ##

The default setting for the minimum number of cysteines to be considered a cysteine rich region is at 5
(Output will contain a "True" or "False" for CRRFound)

To change the number of cysteines considered to be in a cysteine rich region use the option -m ##

# CCRG usage examples

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
./CCRF.py -w 60 -m 6 -f 10 myfastafile.fasta
```
