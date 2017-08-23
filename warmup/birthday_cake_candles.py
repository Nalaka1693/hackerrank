#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    maxn = 0
    count = 1
    for i in range(n):
        if ar[i] > maxn:            
            maxn = ar[i]
            count = 1
        elif maxn == ar[i]:
            count+=1;
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
