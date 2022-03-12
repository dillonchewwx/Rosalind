# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:49:48 2022
@author: dillonchewwx
Solution to kmer on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_kmer.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    kmer_dict = countkmers(4, sequences[0])
    with open("Data/rosalind_kmer_out.txt", 'w') as output:
        output.write(" ".join([str(x) for x in kmer_dict.values()]))

def lexicographically(letters, k):
    import itertools
    return ["".join(x) for x in itertools.product(letters, repeat=k)]

def countkmers(k, sequences):
    # generate library of kmers
    kmer_dict = dict.fromkeys(lexicographically("ACGT", 4), 0)
    for i in range(len(sequences)-k+1):
        kmer_dict[sequences[i:i+k]] += 1
    return(kmer_dict)
    
if __name__ == "__main__":
    main()