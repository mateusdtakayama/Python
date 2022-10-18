mateus = {
    'first_name': 'mateus',
    'last_name': 'takayama',
    'age': 21,
    'city': 'Toledo'
}

print(mateus['first_name'].title())
print(mateus['last_name'].title())
print(mateus['age'])
print(mateus['city'])
print(mateus['first_name'].title()+" "+mateus['last_name'].title())
print('\n')

# Percorrendo todos os pares chave-valor com um laço
for key, value in mateus.items():
    print("key: "+key+" Value: " + str(value))

print('\n')

# Percorrendo todas as chaves de um dicionário com um laço
for name in mateus.keys():
    print(name.title())

friends = ['jen','jeff', 'douglas','anderson']

friends_language = {
    'jen': 'Java',
    'douglas': 'PHP'
}

for name in friends_language:
    print(name.title())
    if name in friends:
        print("Hello, "+name.title()+"! As I can see your favorite language is: "+friends_language[name]+"!")


