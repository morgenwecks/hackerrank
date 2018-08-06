#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    bin1 = []
    bin2 = []
    bin3 = []
    for el in arr:
        if el > 0:
            bin1.append(el)
        elif el < 0:
            bin2.append(el)
        else:
            bin3.append(el)
    print(round(len(bin1)/len(arr),6))
    print(round(len(bin2)/len(arr),6))
    print(round(len(bin3)/len(arr),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
