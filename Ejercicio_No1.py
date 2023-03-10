
from itertools import permutations, product, combinations, combinations_with_replacement
import math

digitos=list(range(10))

listProduct = list(product(digitos,repeat=4))
print('Conteo sucesiones decimales totales: ',len(listProduct))

#A
listPermutations = list(permutations(digitos,4))
print('Conteo sucesiones de 4 digitos diferentes: ',len(listPermutations))

#B
listRepeated = set(listProduct) - set(listPermutations)
print('Conteo sucesiones de 1 o mas digitos repetidos: ',len(listRepeated))

#C
#1
only4Repeated = len({(a,b,c,d) for a,b,c,d in listRepeated if a == b == c == d})
print('Conteo sucesiones de 4 digitos iguales: ',only4Repeated)

#2
only2Repeated = len({(a,a,b,b) for a,b in permutations(digitos,2)}) * int((math.factorial(4)/(math.factorial(2)*math.factorial(2)))/2)
print('Conteo sucesiones de 2 digitos iguales dos veces: ',only2Repeated)

#3
only1Repeated = len(digitos) * len(list(permutations(list(range(1,10)),2))) * int((math.factorial(4)/math.factorial(2))/2)
print('Conteo sucesiones de 2 digitos iguales y 2 digitos diferentes: ',only1Repeated)

#4
triple = len({(a,a,a,b) for a,b in permutations(digitos,2)}) * int(math.factorial(4)/math.factorial(3))
print('Conteo sucesiones de 3 digitos iguales: ',triple)
