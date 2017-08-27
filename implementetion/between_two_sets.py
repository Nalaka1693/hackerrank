#!/bin/python

import sys

def getTotalX(a, b, n, m):
    count = 0
    a.sort()
    b.sort()
    a_ok = 1
    b_ok = 1
    for i in range(a[n-1], b[0] + 1):
        for j in range(n):
            if i % a[j] != 0:
                a_ok = 0
                break              
        for k in range(m):
            if b[k] % i != 0:
                a_ok = 0
                break            
        if a_ok == 1 and b_ok == 1:
            count += 1
        a_ok = 1
        b_ok = 1
    return count

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b, n, m)
    print total
