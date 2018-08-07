#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    la = sorted(arr)
    ld = sorted(arr, reverse = True)

    min = sum(la[:4])
    max = sum(ld[:4])
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
