#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 27th JULY 2019

Description: Program reads file supplied by user, takes an intger value n from user and writes the file contents in new file
without every nth character on each line.
'''

inp_file = open("tupletest")
out_file = open("tempout.txt","w")
size=int(input("Enter character to skip"))
for line in inp_file:
    start = 0
    end = size-1
    while(start<=len(line)):
        out_file.write(line[start:end])
        start=end+1
        end+=size



inp_file.close()
out_file.close()