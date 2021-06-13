"""
Created on Sat Jun 12 19:25:11 2021
@author: dillonchewwx
Solution to ini5 on rosalind.info
"""

def main():
    file = open("rosalind_ini5.txt")
    lines = file.readlines()
    file_out = open("ini5_output.txt", "w")
    count = 1
    for line in lines:
        if count % 2 == 0:
            file_out.write(line)
        count += 1
    file.close()
    file_out.close()
    return 

if __name__ == "__main__":
    main()