#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

a_count = 0
o_count = 0
for i in range(m):
    aa = apple[i] + a
    if aa >= s and aa <= t:
        a_count+=1
for i in range(n):
    oo = orange[i] + b
    if oo >= s and oo <= t:
        o_count+=1
print a_count
print o_count
