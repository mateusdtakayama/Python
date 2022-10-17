lista = ['1', '2','3','4','5','6'',7','8']
print(lista)
print(lista[0])
lista2 = ['mateus','fernando','pedro','marcos']
print(lista2[3].title())
print("Meu nome é "+lista2[0].title())

jantar = ['marcos','pedro','lucas']

print("Olá, "+ jantar[0].title()+ ". Gostaria de jantar hoje?")
jantar[1] = 'joao'
print(jantar)
jantar.insert(0, 'luiz')
print(jantar)
jantar.insert(2, 'maicon')
print(jantar)
jantar.append('jamelao')
print(jantar)
jantar.pop()
print(jantar)
jantar.pop()
print(jantar)
jantar.pop()
print(jantar)
jantar.pop()
print(jantar)
del jantar[0]
print(jantar)
print(jantar[0])
del jantar[0]
print(jantar)


