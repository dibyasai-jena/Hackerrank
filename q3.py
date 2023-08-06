import math
import os
import random
import re
import sys

def timeConversion(s):
    if(s[-2:]=="AM"):
        if(s[:2]=="12"):
            return "00"+s[2:-2]
        else:
            return s[:-2]
    else:
        k = int(s[:2])
        if(k<12):
            k += 12
        return str(k)+s[2:-2]   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
