# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:16:07 2021
@author: dillonchewwx
Solution to sign on rosalind.info
"""

def main():
    with open("Data/rosalind_sign.txt") as file:
        lines = [line.rstrip() for line in file]
    number = int(lines[0])
    output = open("Data/rosalind_sign_out.txt", "w")
    signed_Permutation = signedPermutation(number)
    output.write(str(len(signed_Permutation)))
    output.write('\n')
    for perm in signed_Permutation:
        output.write(" ".join([str(num) for num in perm]))
        output.write("\n")
    output.truncate(output.tell()-2) # remove trailing newline
    output.close()
    file.close()

def signedPermutation(number):
    import itertools
    numlist = [num for num in range(-number, number+1) if num != 0]
    permlist = [perm for perm in itertools.permutations(numlist, number)]
    signedpermlist = []
    for i in range(len(permlist)):
        if len(set([abs(x) for x in permlist[i]])) == number:
            signedpermlist.append(permlist[i])
    return signedpermlist
       
if __name__ == "__main__":
    main()
