import random
a1= str(input("Insira o nome do aluno 1: "))
a2= str(input("Insira o nome do aluno 2: "))
a3= str(input("Insira o nome do aluno 3: "))
a4= str(input("Insira o nome do aluno 4: "))

lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)

print(f"O aluno escolhido foi: {(escolhido)}")