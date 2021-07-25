# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:21:12 2021
@author: dillonchewwx
Solution to long on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_long.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    scs = greedy_scs(sequences, round(len(sequences[0])/2))
    output = open("Data/rosalind_long_out.txt", "w")
    output.write(scs)
    output.close()
    file.close()
    
def pick_maximal_overlap(reads, k):
    """
    Returns a pair of reads from the list with a maximal suffix/prefix overlap >= k. Returns overlap length 0 if there are no such overlaps 
    """
    read_a, read_b = None, None
    best_overlap_length = 0
    
    # make index 
    kmers_set = {}
    for read in reads:
        kmers = getKmer(read, k)
        for kmer in kmers:
            if not kmer in kmers_set.keys():
                kmers_set[kmer] = set()
            kmers_set[kmer].add(read)
    
    for a in reads:
        for b in kmers_set[suffix(a, k)]:
            if a != b:
                overlap_length = overlap(a, b, k)
                if overlap_length > best_overlap_length:
                    read_a, read_b, best_overlap_length = a, b, overlap_length
    return read_a, read_b, best_overlap_length

def greedy_scs(reads, k):
    read_a, read_b, overlap_length = pick_maximal_overlap(reads, k)
    while overlap_length > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[overlap_length:])
        read_a, read_b, overlap_length = pick_maximal_overlap(reads, k)
    return "".join(reads)

def getKmer(read, k):
    kmer = set()
    for i in range(len(read)-k+1):
        kmer.add(read[i:i+k])
    return kmer
        
def prefix(sequence, length):
    return sequence[:length]

def suffix(sequence, length):
    return sequence[-length:]

def overlap(a, b, min_length=3):
    """ 
    Return length of longest suffix of 'a' matching
    a prefix of 'b' that is at least 'min_length'
    characters long.  If no such overlap exists,
    return 0. 
    """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
        
if __name__ == "__main__":
    main()