import math
import os
import random
import re
import sys

def plusMinus(arr):
    c, c1 ,c2 = 0, 0, 0
    
        
    for i in range (n):
        if arr[i]>0 :
            c+=1
            
    print(float(c/n))        
            
       
    for i in range (n):
        if arr[i]<0 :
            c1+=1
     
    print(float(c1/n))
    
    
    for i in range (n):
        if arr[i]==0 :
            c2+=1
            
    print(float(c2/n))        
                   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
