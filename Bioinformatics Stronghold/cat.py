# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:40:36 2021
@author: dillonchewwx
Solution to cat on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_cat.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s = sequences[0]
    print(noncrossingPerfectMatchings(s) % 10**6)
    
def noncrossingPerfectMatchings(s):
    # Takes in an RNA string s having the same number of occurrences of A as U and the same number of C and G and returns the total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000. 
    if s not in table:
        table[s] = sum([noncrossingPerfectMatchings(s[1:i]) * table[s[0]+s[i]] * noncrossingPerfectMatchings(s[i+1:]) for i in range(1, len(s), 2)])
    return table[s]
    
if __name__ == "__main__":
    table = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}
    main()



