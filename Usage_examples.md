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
