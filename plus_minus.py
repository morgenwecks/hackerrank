#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #creating lists for all 3 possible outcomes
    bin1 = []
    bin2 = []
    bin3 = []
    #for each digit in the array:
    for el in arr:
        #if the digit is positive, throw in bin 1
        if el > 0:
            bin1.append(el)
        #if it is negative, throw in bin 2
        elif el < 0:
            bin2.append(el)
        #if it is zero, throw it in bin 3
        else:
            bin3.append(el)
    #print the ratios of the bins vs the total array size, round to 6 digits
    print(round(len(bin1)/len(arr),6))
    print(round(len(bin2)/len(arr),6))
    print(round(len(bin3)/len(arr),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
