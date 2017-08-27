#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'
    else:
        while x1 < x2:
            x1 += v1
            x2 += v2
            if x1 == x2:
                return 'YES'
        return 'NO'

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)


# efficient condition (x1 - x2) % (v2 - v1) == 0, jump times should be a whole number
