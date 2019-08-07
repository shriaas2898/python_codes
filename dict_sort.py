#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 7th August 2019: Added exception handling

Description: Program reads dictionary d which contains student id and room number pair
and creates another dictionary room_ids which contains room number as keys which represent list of students staying in that room
'''

import time

try:
    # declaring dictonary
    d = {1: 101,
         2: 101,
         3: 101,
         4: 102,
         5: 103,
         6: 103,
         7: 102}

    # for checking performance
    tym = time.time()

    # declaring empty dictionary
    room_ids = {}

    for value in set(d.values()):  # Here I have used set() to get the unique elements from list
        room_ids[value] = []  # initializing each key to empty list

    # appending the id to the list
    for key in d.keys():
        room_ids[d[key]].append(key)

    print(room_ids)
    print(time.time() - tym)

except KeyError:
    print("Key doesn't exists")
except NameError:
    print("Dictionary with that name doesn't exists")
except TypeError:
    print("Invalid type used")
except AttributeError:
    print("Invalid Attribute")