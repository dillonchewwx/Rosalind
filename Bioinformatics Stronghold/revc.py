# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:48:55 2021
@author: dillonchewwx
Solution to revc on rosalind.info
"""

def main():
    file = open("rosalind_revc.txt")
    DNAstring = file.read()
    print(reverseComplement(DNAstring))

def reverseComplement(DNAstring):
    trans = DNAstring.maketrans('ACGT', 'TGCA')
    return DNAstring[::-1].translate(trans)

if __name__ == "__main__":
    main()


