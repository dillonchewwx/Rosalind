"""
Created on Sun Jun 13 22:07:11 2021
@author: dillonchewwx
Solution to ini6 on rosalind.info
"""

def main():
    file = open("rosalind_ini6.txt")
    words = file.read().split()
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    file.close()
    for key, value in dict.items():
        print(key, value)
    return 

if __name__ == "__main__":
    main()