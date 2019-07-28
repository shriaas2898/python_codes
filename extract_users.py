#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 28th JULY 2019

Description: Program extracts usernames from  /etc/passwd file and stores in usernames.txt file
'''

#opening passwd file in read mode
inp_file = open("/etc/passwd")
#opening usernames.txt file in write mode
out_file = open ("usernames.txt","w")

#reading file line by line
for line in inp_file:
    #printing extracted username in the file
    out_file.write(line.split(":")[0]+"\n") #since the first value on very line of passwd file is username

#closing connections to the file
inp_file.close()
out_file.close()