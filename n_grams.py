#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 13th August 2019: Added documentation
Description: Program  reads the contents of file 'tempfile.txt', takes user input for number of grams and print the ngrams for the filr
'''

inp_file = open("tempfile.txt")
n = int(input("Enter number grams"))

for line in inp_file:
    count = 0
    words = line.split()
    for word in words[:-n+1]:
        print(" ".join(words[count:count+n]))
        count+=1

inp_file.close()
