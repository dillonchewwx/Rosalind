# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:37:24 2021
@author: dillonchewwx
Solution to dna on rosalind.info
"""
def main():
    file = open("Data/rosalind_dna.txt")
    DNAstring = file.read()
    print(countBases(DNAstring))

def countBases(DNAstring):
    dict = {}
    for base in DNAstring:
        if base in dict:
            dict[base] += 1
        else: 
            dict[base] = 1
    return(dict['A'], dict['C'], dict['G'], dict['T'])
    

if __name__ == "__main__":
    main()

