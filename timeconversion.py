#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ss = s[:2]

    if int(ss) < 12 and 'AM' in s :
        return(s[:-2])

    elif int(ss) == 12 and 'PM' in s:
        return(ss+s[2:-2])

    elif int(ss) == 12 and 'AM' in s:
        return('00'+s[2:-2])

    elif int(ss) < 12 and 'PM' in s:
        return((str(int(ss) + 12)) + s[2:-2])
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
