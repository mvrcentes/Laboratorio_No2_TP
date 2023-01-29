# Universidad del Valle de Guatemala
# Teoria de Probabilidades
# Laboratorio #2 - Problema #2

numsone2hundred = set([i for i in range(2, 100)])
numsone2hundred_NoPrimos = set()
primosone2ten = set([2,3,5,7])

for i in primosone2ten: 
    for j in numsone2hundred:
        if j % i == 0:
            numsone2hundred_NoPrimos.add(j)

numsone2hundred -= numsone2hundred_NoPrimos 
numsone2hundred.update(primosone2ten)

print(f'\nLos numeros primos entre 1 y 100 son:\t{len(numsone2hundred)}\n')
print('Y son:')
print(numsone2hundred)


