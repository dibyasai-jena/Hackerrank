import math
import os
import random
import re
import sys
def miniMaxSum(arr):
    i, j, temp, maxsum, minsum = 0 , 1 , 0 , 0 , 0
    for i in range (5):
        for j in range (5):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    for i in range(1,5):
        minsum += arr[i]
        
    for i in range(0,4):
        maxsum += arr[i]
        
    print(minsum, end=" ")
    print(maxsum)   
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
