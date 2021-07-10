# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:27:03 2021
@author: dillonchewwx
Solution to orf on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_orf.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    output = open("Data/rosalind_orf_out.txt", 'w')
    for sequence in sequences:
        res = [prot_seq for prot_seq in orf(sequence)]
        for prot in res:
            output.write(str(prot))
            output.write("\n")
    output.truncate(output.tell()-2) # remove trailing newline
    output.close()
    file.close()

def orf(sequence):
    # orf takes in a DNA sequence and returns all possible protein strings that can be translated from all open reading frames. 
    import revc, rna, prot
    import re
    orfs = []
    fwdrna = rna.DNAtoRNA(sequence)
    revcomprna = rna.DNAtoRNA(rna.DNAtoRNA(revc.reverseComplement(sequence)))
    orfs += re.findall("(?=(AUG(?:...)*?)(UAA|UAG|UGA))", fwdrna) 
    orfs += re.findall("(?=(AUG(?:...)*?)(UAA|UAG|UGA))", revcomprna)
    orfs_list = [''.join(x) for x in orfs]
    prot_list = [prot.translation(aa) for aa in list(orfs_list)]
    return(list(set(prot_list)))

if __name__ == "__main__":
    main()

