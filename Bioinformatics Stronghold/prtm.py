# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:40:31 2021
@author: dillonchewwx
Solution to prtm on rosalind.info
"""
def main():
    file = open("Data/rosalind_prtm.txt")
    prot_seq = file.read().splitlines(0)
    print(proteinSequencetoMass(prot_seq[0]))
    file.close()

def proteinSequencetoMass(prot_seq):
    # Function takes in a single protein sequence and returns the combined mass of its amino acids.
    # load Monoisotopic mass table (Da)
    AA_to_mass = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }
    mass = 0
    for aa in prot_seq:
        mass += AA_to_mass[aa]
    return round(mass, 3)
    
if __name__ == "__main__":
    main()

