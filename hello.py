# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    for i in [a,b,c]:
        if not isinstance(i,(float,int)):
            raise TypeError('Bad type')
    m = b ** 2 - 4*a*c
    if m < 0:
        print('方程无实根')
    elif m == 0:
        print('方程只有一个实根')
        return -b/2*a
    else:
        x2 = (-b+math.sqrt(m))/2*a
        x3 = (-b-math.sqrt(m))/2*a
        print('方程有两个实根')
        return x2, x3

print(quadratic(1,4,3))

