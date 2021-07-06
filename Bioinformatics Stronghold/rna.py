# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:46:23 2021
@author: dillonchewwx
Solution to rna on rosalind.info
"""

def main():
    file = open("Data/rosalind_rna.txt")
    DNAstring = file.read()
    print(DNAtoRNA(DNAstring))

def DNAtoRNA(DNAstring):
    RNAstring = DNAstring.replace('T', 'U')
    return(RNAstring)

if __name__ == "__main__":
    main()


