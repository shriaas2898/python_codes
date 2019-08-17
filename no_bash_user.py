#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 17th August 2019
Description: Program print usernames of users where default shell is not bash from  /etc/passwd file
'''

try:
    # opening passwd file in read mode
    inp_file = open("/etc/passwd")

    # reading file line by line
    for line in inp_file:
        # printing required  usernames
        if "bash" not in line:
            print(line.split(":")[0])




except FileNotFoundError:
    print("/etc/passwd not found")

except PermissionError:
    print("Permission denied to read file")

except IsADirectoryError:
    print("Requested file is a directory")

finally:
    try:
        inp_file.close()

    except AttributeError:
        pass