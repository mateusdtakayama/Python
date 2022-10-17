car = 'subaru'
print("Car == 'subaro'? Eu acho que sim")

print(car == 'subaru')
print(car == 'audi')

age = 12

if age < 4:
    prince = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("your admission cost is  $" + str(price)+ ".")

lista = ['subaru','ferrari', 'corsa','fusca']

if 'fusca' in lista:
    print("I found it in " + str(lista.index('fusca')))

alien_color = 'red'

if alien_color == 'green':
    print("you won 5 points")

elif alien_color == 'red':
    print("you lost 10 points")

else:
    print("nothing happened")

age = 13

if age < 2:
    print("you're a baby")
elif age >= 2 and age < 4:
    print("you're a kid")
elif age >= 4 and age < 13:
    print("you're a boy")
elif age >= 13 and age < 20:
    print("you'are a teenager")
elif age >= 20 and age < 65:
    print("you're a adult")
else:
    print("you're a old man")

frutas = ['banana', 'apple', 'pear']

for fruta in frutas:
    print("you really like "+ fruta)
    