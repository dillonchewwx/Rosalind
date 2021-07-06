# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:50:42 2021
@author: dillonchewwx
Solution to gc on rosalind.info
"""

def main():
    file = open("Data/rosalind_gc.txt")
    dict = {}
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            words = line.split()
            name = words[0][1:]
            dict[name] = ''
        else:
            dict[name] += line
    file.close()
    
    gc = {key:gcContent(dict[key]) for key in dict}
    print(max(gc, key=gc.get), gc[max(gc, key=gc.get)]*100, sep='\n')


def gcContent(dna):
    return (dna.count('C') + dna.count('G'))/len(dna)

if __name__ == "__main__":
    main()


