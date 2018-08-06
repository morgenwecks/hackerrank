#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    #initial values for left and right diagonal sum
    left = 0
    right = 0
    
    #give me positions of the rows in my matrix
    for counter, value in enumerate(arr):
        
        #left gets added the corresponding value of my row's counter
        left += value[counter]
        
        #right is the reverse
        rights = value[::-1]
        right += rights[counter]
        
    #we want the absolute difference
    result = abs(left-right)
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
