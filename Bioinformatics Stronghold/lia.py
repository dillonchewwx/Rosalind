# -*- coding: utf-8 -*-
"""
Created on Wed Jul 7 23:41:16 2021
@author: dillonchewwx
Solution to lia on rosalind.info
"""
def main():
    file = open("Data/rosalind_lia.txt")
    numbers = file.read().split(' ')
    k = int(numbers[0])
    n = int(numbers[1])
    print(mendel_second_law(k, n)) 
    file.close()
    
def mendel_second_law(k, n):
    # k is the generation number
    # n is the number of Aa Bb 
    # We need to calculate the probability that at least n Aa Bb organisms will belong to the k-th generation if at each generation, an Aa Bb will mate with an Aa Bb and have two offspring. 
    # Probablity of getting AaBb when AaBb x AaBb is 1/4. 
    # This can be modelled as a binomial distribution with number of trials = 2k and number of successes = n. The probability of achieving at least n organisms would then be the cumulative probability P(X>=x).
    from scipy.stats import binom
    # As the binom.cdf function returns P(X<=x), we take the complementary.
    return round(1-binom.cdf(n-1, 2**k, 0.25), 3)

if __name__ == "__main__":
    main()