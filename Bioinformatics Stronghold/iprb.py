# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 01:38:52 2021
@author: dillonchewwx
Solution to iprb on rosalind.info
"""

def main():
    file = open("rosalind_iprb.txt")
    numbers = file.read().split(' ')
    k = int(numbers[0])
    m = int(numbers[1])
    n = int(numbers[2])
    file.close()
    print(mendelFirstLaw(k, m, n))    
    
# We consider the cases where we will get the recessive phenotype, then take the complement to get the dominant phenotype. =============================================================================
# If two homozygous recessive mates (aa x aa), the probability of getting a recessive offspring is 1. 
# If a heterozygous mates with a homozygous recessive (Aa x aa), the probablity of getting a recessive offspring is 1/2. 
# If two heterozygous mates (Aa x Aa), the probability of getting a recessive offspring is 1/4.  =============================================================================

def mendelFirstLaw(k, m, n):
    total = k+m+n
    p_nn = n/total * (n-1)/(total-1)
    p_nm = n/total * (m/(total-1)) * 1/2
    p_mn = m/total * (n/(total-1)) * 1/2
    p_mm = m/total * ((m-1)/(total-1)) * 1/4
    return 1-(p_nn+p_nm+p_mn+p_mm)

if __name__ == "__main__":
    main()
