#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
arr.sort()
print sum(arr[:4]), sum(arr[1:])
