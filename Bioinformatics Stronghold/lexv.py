# -*- coding: utf-8 -*-
"""
Created on Mon Apr 4 01:10:18 2022
@author: dillonchewwx
Solution to lexv on rosalind.info
"""
def main():
    file = open("Data/rosalind_lexv.txt")
    lines = file.read().splitlines()
    letters = lines[0].replace(" ", "")
    length = int(lines[1])
    output = open("Data/rosalind_lexv_out.txt", "w")
    res = orderedLexicographically(letters, length)
    for x in res:
        output.write("".join(x))
        output.write("\n")
    output.truncate(output.tell()-2)
    output.close()
    file.close()

def orderedLexicographically(letters, length):
    import itertools
    output = []
    for i in itertools.product(letters, repeat=length):
        for j in range(1, length+1):
            if i[:j] not in output:
                output.append(i[:j])
    return(output)

if __name__ == "__main__":
    main()


