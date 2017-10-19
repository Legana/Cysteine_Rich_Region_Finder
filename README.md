# Cysteine rich region finder (CCRF)

Default settings are to count the maximum number of cysteines in a window size of 30 advancing by 1 frame (amino acid) at a time

To change the window size use the option -w ##
To change the frame size use the option -f ##

The default setting for the minimum number of cysteines to be considered a cysteine rich region is at 5
(Output will contain a "True" or "False" for CRRFound)

To change the number of cysteines considered to be in a cysteine rich region use the option -m ##
