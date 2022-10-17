magos = ['elo','gorn','alfred','peer']

for mago in magos:
    print(mago)

for mago in magos:
    print("O mago "+mago+" é bom")

for num in range(1,21):
    print(num)

numeros = list(range(1,1000001))

for numero in numeros:
    print(numero)

print(max(numeros))
print(min(numeros))
print(sum(numeros))

numeros = list(range(1,21,2))

for numero in numeros:
    print(numero)

numeros = list(range(3,31,3))

for numero in numeros:
    print(numero)

for valor in range(1,11):
    numeros.append(valor**3)

for valor in numeros:
    print(valor)

print("list comprehensions")

cubos = [value**3 for value in range(1,11)]
print(cubos)
