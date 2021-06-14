# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 01:38:52 2021
@author: dillonchewwx
Solution to hamm on rosalind.info
"""

def main():
    file = open("rosalind_iprb.txt")
    numbers = file.read().split(' ')
    k = int(numbers[0])
    m = int(numbers[1])
    n = int(numbers[2])
    file.close()
    print(mendelFirstLaw(k, m, n))    
    
# There are 4 different cases in this scenario =============================================================================
# Two homozygous dominant mating will always result in dominant phenotype. Likewise, two homozygous recessive mating will always result in a recessive phenotype. 
# When heterozygous mates with a homozygous dominant, it always results in a dominant phenotype. 
# However, when a heterozygous mates with a homozygous recessive, there is a 1/4 probablity that it will result in a dominant phenotype, and a 3/4 probabilty that it will result in a recessive phenotype.
# When two heterozygous mates, there is a 3/4 probability of the offspring possessing a dominant phenotype, and a 1/4 probability of posessing a recessive phenotype.  
# We calculate the probability of getting a recessive, then take the complement to get the probability of getting a dominant.  =============================================================================

def mendelFirstLaw(k, m, n):
    total = k+m+n
    p_nn = n/total * (n-1)/(total-1)
    p_nm = n/total * (m/(total-1)) * 1/2
    p_mn = m/total * (n/(total-1)) * 1/2
    p_mm = m/total * ((m-1)/(total-1)) * 1/4
    return 1-(p_nn+p_nm+p_mn+p_mm)

if __name__ == "__main__":
    main()
