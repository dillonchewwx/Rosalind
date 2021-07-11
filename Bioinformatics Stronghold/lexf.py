# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:56:23 2021
@author: dillonchewwx
Solution to lexf on rosalind.info
"""
def main():
    file = open("Data/rosalind_lexf.txt")
    lines = file.read().splitlines()
    letters = lines[0].replace(" ", "")
    length = int(lines[1])
    output = open("Data/rosalind_lexf_out.txt", "w")
    res = lexicographically(letters, length)
    for x in res:
        output.write("".join(x))
        output.write('\n')
    output.truncate(output.tell()-2)
    output.close()
    file.close()
    
def lexicographically(letters, length):
    import itertools
    return list(itertools.product(letters, repeat=length))

if __name__ == "__main__":
    main()

