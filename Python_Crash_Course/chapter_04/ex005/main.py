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

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

print("Esses são os primerios jogadores do time: \n")
for player in players[:3]:
    print(player.title())

players2 = ["pedro"]

players2 = players[:]

players2.append("micao")
players2.append("jao")
print(players)
print(players2)

print(players2[:3])
print(players2[2:5])
print(players2[-3:])
print(players2)

minhas_pizzas = ['vegetariana', 'strogonoff','abacaxi nevado']

pizzas_amigo = minhas_pizzas[:]

minhas_pizzas.append('carne')
pizzas_amigo.append('chocolate')

print(minhas_pizzas)
print(pizzas_amigo)

for sabores in minhas_pizzas:
    print(sabores)

