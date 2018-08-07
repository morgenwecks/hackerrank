#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    l = ['#']*n
    for position, char in enumerate(l):
        print(' ' * (len(l)-(position+1)) + ((position+1)*char))

if __name__ == '__main__':
    n = int(input())

    staircase(n)