# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:57:01 2022
@author: dillonchewwx
Solution to mmch on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_mmch.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s = sequences[0]
    print(maximumMatchings(s))

def maximumMatchings(s):
    # We can just look at A-U matches and C-G matches separately.
    au_min, au_max = sorted([s.count("A"), s.count("U")])
    gc_min, gc_max = sorted([s.count("G"), s.count("C")])
    
    # Number of possible A-U pairings is just max(AU)!/abs(A-U)!
    # Same goes for GC. 
    # Multiply both numbers to give the maximum number of matches. 
    from math import factorial
    res = factorial(au_max)//factorial(au_max-au_min) * factorial(gc_max)//factorial(gc_max-gc_min)
    return(int(res))
    
if __name__ == "__main__":
    main()




