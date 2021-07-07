# -*- coding: utf-8 -*-
"""
Created on Thu Jul 8 00:25:34 2021
@author: dillonchewwx
Solution to mprt on rosalind.info
"""
def main():
    file = open("Data/rosalind_mprt.txt")
    uniprot_ids = file.read().splitlines()
    output = open("Data/rosalind_mprt_out.txt", 'w')
    for key, value in motifLocationInProtein(uniprot_ids).items():
        output.write("".join(str(key) + "\n"))
        output.write(" ".join(str(item) for item in value) + "\n")
    output.truncate(output.tell()-2) # remove trailing newline
    output.close()
    file.close()

def motifLocationInProtein(uniprot_ids):
    # For each protein possessing the N-glycosylation motif of N{P}[ST]{P}, output its given access ID followed by a list of locations in the protein string where the motif can be found.
    # {P} : anything but P
    # [ST] : either S or T
    # Fasta files for each protein can be accessed on the uniprot website at  can be accessed at http://www.uniprot.org/uniprot/uniprot_id.fasta
    from Bio import SeqIO
    from io import StringIO
    import requests
    import regex as re
    dict = {}
    for uniprot_id in uniprot_ids:
        url = "".join(["http://www.uniprot.org/uniprot/", str(uniprot_id), ".fasta"])
        data = requests.get(url).text
        fasta = SeqIO.parse(StringIO(data), "fasta")
        prot_seq = [str(sequence.seq) for sequence in list(fasta)]
        if len(re.findall("N[^P][T|S][^P]", str(prot_seq[0]), overlapped=True)) >= 1:
           dict[str(uniprot_id)] = [1+int(prot_seq[0].index(motif)) for motif in re.findall("N[^P][ST][^P]", str(prot_seq[0]), overlapped=True)]
    return dict
    
if __name__ == "__main__":
    main()