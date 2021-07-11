# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:26:53 2021
@author: dillonchewwx
Solution to splc on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_splc.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    print(spliceAndTranslate(sequences))
    file.close()

def spliceAndTranslate(sequences):
    # Takes in a list of sequences where the first sequence is a DNA string and the following sequences are introns. Function returns a protein string resulting from transcribing and translating the exons of the DNA string.
    dnastring = sequences.pop(0)
    import subs, rna, prot
    # use subs to find index of intron in dna sequence
    # use rna and prot to transcribe and translate
    for sequence in sequences:
        intron_ind = int(subs.motifFinder(dnastring, sequence))
        dnastring = dnastring[:intron_ind-1]+ dnastring[intron_ind+len(sequence)-1:] # delete introns
    return(prot.translation(rna.DNAtoRNA(dnastring)))
    
if __name__ == "__main__":
    main()
