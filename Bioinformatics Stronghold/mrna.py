# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:55:09 2021
@author: dillonchewwx
Solution to mrna on rosalind.info
"""
def main():
    file = open("Data/rosalind_mrna.txt")
    prot_seq = file.read().splitlines()
    print(RNAStringsfromProtein(prot_seq[0]))
    file.close()

def RNAStringsfromProtein(prot_seq):
    # load RNA codon table
    RNA_to_AA = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }
    
    from collections import Counter
    AACounts = Counter(RNA_to_AA.values())
    num = 1
    mod = 1000000
    for aa in prot_seq:
        num = ((num * int(AACounts[aa])) % mod + mod) % mod
    num = ((num*3) % mod + mod) % mod # stop codon
    return(num)
    
if __name__ == "__main__":
    main()
