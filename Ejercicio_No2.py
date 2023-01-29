from itertools import permutations, product, combinations, combinations_with_replacement
import math

n = ((100-7)+1);

primeraSumatoria = 0;
primosone2ten = set([2, 3, 5, 7])
for i in primosone2ten:
 primeraSumatoria += (n//i)

segundaSumatoria = 0;
for i, j in list(combinations(primosone2ten, 2)):
 segundaSumatoria += (n // math.lcm(i, j))

terceraSumatoria = 0;
for i, j, k in list(combinations(primosone2ten, 3)):
 terceraSumatoria += (n // math.lcm(i, j, k))

cuartaSumatoria = 0;
for i, j, k, l in list(combinations(primosone2ten, 4)):
 cuartaSumatoria += (n // math.lcm(i, j, k, l))

principio_inclusion_exclusion = n-primeraSumatoria+segundaSumatoria-terceraSumatoria+cuartaSumatoria
print('Los primos entre 1 y 100 son: ',principio_inclusion_exclusion+len(primosone2ten))

numsone2hundred = set([i for i in range(2, 100)])
numsone2hundred_NoPrimos = set()

for i in primosone2ten:
 for j in numsone2hundred:
  if j % i == 0:
   numsone2hundred_NoPrimos.add(j)

numsone2hundred -= numsone2hundred_NoPrimos
numsone2hundred.update(primosone2ten)
print('Y son:')
print(sorted(numsone2hundred))
