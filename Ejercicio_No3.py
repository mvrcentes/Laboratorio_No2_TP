# Universidad del Valle de Guatemala
# Teoria de Probabilidades
# Laboratorio #2 - Problema #3

from itertools import *

n = 7
m = 5
k = 0

lista = []
conjunto = [1, 2, 3, 4, 5, 6, 7]
for i1 in range(1, n+1):
    for i2 in range(1, i1+1):
        for i3 in range(1, i2+1):
            for i4 in range(1, i3+1):
                for i5 in range(1, i4+1):
                    lista.append((i5, i4, i3, i2, i1))
                    k += 1
print(k)
print(len(list(combinations_with_replacement(conjunto, m))))
        