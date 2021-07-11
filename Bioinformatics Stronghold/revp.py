# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:23:06 2021
@author: dillonchewwx
Solution to revp on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_revp.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    output = open("Data/rosalind_revp_out.txt", "w")
    for sequence in sequences:
        res = reversePalindrome(sequence)
    for pair in res:
        output.write(" ".join([str(x) for x in pair]))
        output.write("\n")
    output.truncate(output.tell()-2) # remove trailing newline
    output.close()
    file.close()

def reversePalindrome(sequence):
    # Takes in a DNA string and returns the position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
    list = []
    for i in range(4,13,2):
        for j in range(0, len(sequence)-i+1):
            if sequence[j:j+int(i/2)] == reverseComplement(sequence[j+int(i/2):j+i]):
                list.append([j+1,i])# sliding window of length i
    return list

def reverseComplement(DNAstring):
    trans = DNAstring.maketrans('ACGT', 'TGCA')
    return DNAstring[::-1].translate(trans) 
    
if __name__ == "__main__":
    main()