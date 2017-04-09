# Programmet loser andragradsekvationer pa formen
# -*- coding: utf-8 -*-
# x^2 + px + q = 0

import math
import cmath

print("x\u00b2 + px + q = 0")
print("___________________")

p = float(input("P= "))
q = float(input("Q= "))

d = -p/2
root = d**2-q
if root != 0:
    if root  < 0:
        # Ingen reell l?sning
        print("x1 = " + str(d + cmath.sqrt(root)))
        print("x2 = " + str(d - cmath.sqrt(root)))
    else:
        print("x1 = " + str(d+ math.sqrt(root)))
        print("x2 = " + str(d- math.sqrt(root)))

else:
    print("x = " + str(d))

print("Slut")